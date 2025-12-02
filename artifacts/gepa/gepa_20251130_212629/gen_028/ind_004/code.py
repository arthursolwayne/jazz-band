
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums, with subtle fills and space

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 64, 100), # F
    (1.75, 65, 100), # Gb
    (2.0, 65, 100), # Gb
    (2.25, 64, 100), # F
    (2.5, 62, 100), # Eb
    (2.75, 64, 100), # F
    (3.0, 65, 100), # Gb
    (3.25, 65, 100), # Gb
    (3.5, 64, 100), # F
    (3.75, 62, 100), # Eb
    (4.0, 64, 100), # F
    (4.25, 65, 100), # Gb
    (4.5, 65, 100), # Gb
    (4.75, 64, 100), # F
    (5.0, 62, 100), # Eb
    (5.25, 64, 100), # F
    (5.5, 65, 100), # Gb
    (5.75, 65, 100), # Gb
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    (2.0, 64, 110), # F
    (2.0, 67, 110), # A
    (2.0, 69, 110), # C
    (2.0, 71, 110), # D
    # Bar 3: Bb7 on beat 2
    (3.0, 62, 110), # Bb
    (3.0, 65, 110), # D
    (3.0, 67, 110), # E
    (3.0, 71, 110), # G
    # Bar 4: F7 on beat 2
    (4.0, 64, 110), # F
    (4.0, 67, 110), # A
    (4.0, 69, 110), # C
    (4.0, 71, 110), # D
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: motif in F, with space and tension
# Start with a short phrase, leave it hanging
sax_notes = [
    (1.5, 66, 110), # G
    (1.625, 69, 110), # Bb
    (1.75, 66, 110), # G
    (1.875, 64, 110), # F
    (2.0, 66, 110), # G
    (2.125, 69, 110), # Bb
    (2.25, 66, 110), # G
    (2.375, 64, 110), # F
    (3.0, 66, 110), # G
    (3.125, 69, 110), # Bb
    (3.25, 66, 110), # G
    (3.375, 64, 110), # F
    (3.5, 66, 110), # G
    (3.625, 69, 110), # Bb
    (3.75, 66, 110), # G
    (3.875, 64, 110), # F
    (4.0, 66, 110), # G
    (4.125, 69, 110), # Bb
    (4.25, 66, 110), # G
    (4.375, 64, 110), # F
    (4.5, 66, 110), # G
    (4.625, 69, 110), # Bb
    (4.75, 66, 110), # G
    (4.875, 64, 110), # F
    (5.0, 66, 110), # G
    (5.125, 69, 110), # Bb
    (5.25, 66, 110), # G
    (5.375, 64, 110), # F
    (5.5, 66, 110), # G
    (5.625, 69, 110), # Bb
    (5.75, 66, 110), # G
    (5.875, 64, 110), # F
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Add rests and space in sax
# No notes at:
# 1.5 - 1.625 (rest)
# 2.375 - 3.0 (rest)
# 3.875 - 4.0 (rest)
# 4.875 - 5.0 (rest)
# 5.875 - 6.0 (rest)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
