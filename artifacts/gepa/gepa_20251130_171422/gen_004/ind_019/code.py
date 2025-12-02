
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar length in seconds (160 BPM, 4/4 time => one bar = 1.5 seconds)
bar_length = 1.5
beat_length = 0.375  # 160 BPM => 60/160 = 0.375s per beat

# BAR 1: Little Ray on drums only - build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * beat_length
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + beat_length)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + beat_length)
        drums.notes.append(note)
    # Hi-hat on every eighth
    for eighth in range(2):
        hihat_time = time + eighth * beat_length / 2
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['hihat'], start=hihat_time, end=hihat_time + (beat_length / 2) - 0.01)
        drums.notes.append(note)

# BAR 2: Everyone in. Sax takes the melody.
# Bar starts at 1.5s (end of first bar)
bar_start = 1.5

# Bass line - walking line, chromatic approaches
bass_notes = [
    (bar_start + 0.0, 62),  # F
    (bar_start + 0.375, 63),  # Gb
    (bar_start + 0.75, 60),  # E
    (bar_start + 1.125, 59),  # Eb

    (bar_start + 1.5, 62),  # F
    (bar_start + 1.875, 63),  # Gb
    (bar_start + 2.25, 60),  # E
    (bar_start + 2.625, 59),  # Eb
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp with emotion
# F7 = F A C Eb
# Fm7 = F Ab Bb D
# Start at bar_start (1.5s)
piano_notes = [
    # Bar 2 (beat 2)
    (bar_start + 0.75, 64),  # F
    (bar_start + 0.75, 70),  # A
    (bar_start + 0.75, 69),  # C
    (bar_start + 0.75, 67),  # Eb
    # Bar 2 (beat 4)
    (bar_start + 1.5, 64),  # F
    (bar_start + 1.5, 69),  # Ab
    (bar_start + 1.5, 67),  # Bb
    (bar_start + 1.5, 62),  # D
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Saxophone melody: short, striking motif. Start on beat 1.5s
# F - Bb - F - rest (F is the tonic, Bb is the b7)
# Motif: F (beat 1), Bb (beat 2), F (beat 3), rest (beat 4)
sax_notes = [
    (bar_start + 0.0, 64),  # F
    (bar_start + 0.375, 67),  # Bb
    (bar_start + 0.75, 64),  # F
    (bar_start + 1.125, 64),  # F (overlap for phrasing)
    (bar_start + 1.5, 64),   # F (end of bar)
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_intro.mid")
