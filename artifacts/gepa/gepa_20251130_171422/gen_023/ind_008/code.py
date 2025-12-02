
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create tension with sparse, syncopated rhythm
drum_notes = [
    (0.0, 36, 100),   # Kick on beat 1
    (0.75, 42, 80),   # Hihat on & of 1
    (1.0, 38, 110),   # Snare on beat 2
    (1.25, 42, 80),   # Hihat on & of 2
    (1.5, 36, 100),   # Kick on beat 3
    (1.75, 42, 80),   # Hihat on & of 3
    (2.0, 38, 110),   # Snare on beat 4
    (2.25, 42, 80),   # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: F, G#, Bb, Ab (start on beat 1)
sax_notes = [
    (1.5, 77, 100),   # F (beat 1)
    (1.75, 81, 100),  # G# (beat 2)
    (2.0, 79, 100),   # Bb (beat 3)
    (2.25, 76, 100),  # Ab (beat 4)
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: F, G, Bb, Ab (walking with chromatic passing)
bass_notes = [
    (1.5, 67, 80),    # F
    (1.75, 68, 80),   # G
    (2.0, 69, 80),    # Ab (chromatic passing)
    (2.25, 70, 80),   # Bb
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on beat 2 and 4
piano_notes = [
    (1.75, 64, 90),   # F7 (F, A, C, Eb)
    (2.25, 64, 90),   # F7 (F, A, C, Eb)
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif variation: F, Bb, G#, Ab (start on beat 1)
sax_notes = [
    (3.0, 77, 100),   # F (beat 1)
    (3.25, 79, 100),  # Bb (beat 2)
    (3.5, 81, 100),   # G# (beat 3)
    (3.75, 76, 100),  # Ab (beat 4)
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: F, Eb, G, Ab (walking with chromatic passing)
bass_notes = [
    (3.0, 67, 80),    # F
    (3.25, 65, 80),   # Eb
    (3.5, 68, 80),    # G
    (3.75, 70, 80),   # Ab
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on beat 2 and 4
piano_notes = [
    (3.25, 64, 90),   # F7 (F, A, C, Eb)
    (3.75, 64, 90),   # F7 (F, A, C, Eb)
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif resolution: F, Ab, Bb, G# (start on beat 1)
sax_notes = [
    (4.5, 77, 100),   # F (beat 1)
    (4.75, 76, 100),  # Ab (beat 2)
    (5.0, 79, 100),   # Bb (beat 3)
    (5.25, 81, 100),  # G# (beat 4)
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: F, G, Ab, Bb (walking with chromatic passing)
bass_notes = [
    (4.5, 67, 80),    # F
    (4.75, 68, 80),   # G
    (5.0, 70, 80),    # Ab
    (5.25, 71, 80),   # Bb
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on beat 2 and 4
piano_notes = [
    (4.75, 64, 90),   # F7 (F, A, C, Eb)
    (5.25, 64, 90),   # F7 (F, A, C, Eb)
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: full rhythm
drum_notes = [
    (4.5, 36, 100),   # Kick on beat 1
    (4.75, 42, 80),   # Hihat on & of 1
    (5.0, 38, 110),   # Snare on beat 2
    (5.25, 42, 80),   # Hihat on & of 2
    (5.5, 36, 100),   # Kick on beat 3
    (5.75, 42, 80),   # Hihat on & of 3
    (6.0, 38, 110),   # Snare on beat 4
    (6.25, 42, 80),   # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
