
import pretty_midi

# Initialize MIDI object with tempo (160 BPM)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            # Kick on beat 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.375)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on beat 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.375)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.1875)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start of the melody (sax), bass walking, piano comping

# Time for bar 2 (1.5s)
bar_start = 1.5

# SAX: Tenor sax melody (Fm key, motif)
# Fm7 chord: F, Ab, Bb, D
# Motif: F, Ab, Bb, D (chromatic approach to Bb)
# Start with F, then Ab, then Bb, then D — but leave it hanging on D

sax_notes = [
    (bar_start + 0.0, 77),  # F (F4)
    (bar_start + 0.375, 79), # Ab (Ab4)
    (bar_start + 0.75, 78),  # Bb (Bb4)
    (bar_start + 1.125, 82), # D (D4)
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# BASS: Walking line in Fm (F, Ab, Bb, D)
# Chromatic approach to F

bass_notes = [
    (bar_start + 0.0, 64),  # F2 (F)
    (bar_start + 0.375, 63), # Eb2 (chromatic approach)
    (bar_start + 0.75, 65),  # F#2 (chromatic approach)
    (bar_start + 1.125, 64), # F2 (resolve)
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# PIANO: Comping on 2 and 4 with 7th chords in Fm
# Fm7: F, Ab, Bb, D (F7 alternative: F, Ab, Bb, C)

piano_notes = [
    (bar_start + 0.75, 77),  # F
    (bar_start + 0.75, 80),  # Ab
    (bar_start + 0.75, 78),  # Bb
    (bar_start + 0.75, 82),  # D
    (bar_start + 1.5, 77),  # F
    (bar_start + 1.5, 80),  # Ab
    (bar_start + 1.5, 78),  # Bb
    (bar_start + 1.5, 82),  # D
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Drums continue for all bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(2, 4):
    for beat in range(4):
        time = bar_start + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            # Kick on beat 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.375)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on beat 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.375)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.1875)
        drums.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to a MIDI file
midi.write("dante_introduction.mid")
