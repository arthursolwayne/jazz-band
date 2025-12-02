
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# MIDIClock: 160 BPM => 60 / 160 * 1000 = 375ms per beat
beat = 0.375  # seconds
bar = 4 * beat  # 1.5 seconds per bar
total_time = 4 * bar  # 6.0 seconds total

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_index in range(1):
    start_time = bar_index * bar
    # Kick on 1 and 3
    for kick_beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=start_time + kick_beat * beat, end=start_time + kick_beat * beat + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for snare_beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=start_time + snare_beat * beat, end=start_time + snare_beat * beat + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for hihat_beat in range(8):
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=start_time + hihat_beat * beat / 2, end=start_time + hihat_beat * beat / 2 + 0.05)
        drums.notes.append(note)

# BAR 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): walking line with chromatic approaches
bass_notes = [
    # Bar 2: D - Eb - F - G (in D minor)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + beat),
    pretty_midi.Note(velocity=90, pitch=63, start=1.5 + beat, end=1.5 + 2 * beat),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 2 * beat, end=1.5 + 3 * beat),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3 * beat, end=1.5 + 4 * beat),
    # Bar 3: A - Bb - C - D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 4 * beat, end=1.5 + 5 * beat),
    pretty_midi.Note(velocity=90, pitch=70, start=1.5 + 5 * beat, end=1.5 + 6 * beat),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5 + 6 * beat, end=1.5 + 7 * beat),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5 + 7 * beat, end=1.5 + 8 * beat),
    # Bar 4: D - Eb - F - G (same as bar 2, chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 8 * beat, end=1.5 + 9 * beat),
    pretty_midi.Note(velocity=90, pitch=63, start=1.5 + 9 * beat, end=1.5 + 10 * beat),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 10 * beat, end=1.5 + 11 * beat),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 11 * beat, end=1.5 + 12 * beat)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# Dm7 (D-F-A-C) on beat 2 and 4 of each bar
# Use descending 7th chords on beats 2 and 4
chords = [
    [62, 64, 67, 70],  # Dm7
    [62, 64, 67, 70],  # Dm7
    [62, 64, 67, 70],  # Dm7
    [62, 64, 67, 70],  # Dm7
]

for bar_index in range(2, 5):
    start_time = (bar_index - 2) * bar + 1.5
    for beat_index in [1, 3]:
        for note in chords[bar_index - 2]:
            piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start_time + beat_index * beat, end=start_time + beat_index * beat + 0.1)
            piano.notes.append(piano_note)

# Sax (Dante): short motif, make it sing
# Start on D (62), move to F (64), resolve to G (67)
# First note on 1, leave it hanging, return on 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.25),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.5 + beat, end=1.5 + beat + 0.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 2 * beat, end=1.5 + 2 * beat + 0.25),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_sax_intro.mid')
