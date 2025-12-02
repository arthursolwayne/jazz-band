
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 1.0, 1.0),  # Kick on 1
    (42, 1.0, 1.0),  # Hihat on 1
    (38, 1.5, 1.0),  # Snare on 2
    (42, 1.5, 1.0),  # Hihat on 2
    (36, 2.0, 1.0),  # Kick on 3
    (42, 2.0, 1.0),  # Hihat on 3
    (38, 2.5, 1.0),  # Snare on 4
    (42, 2.5, 1.0)   # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: Walking line, chromatic approach to D
bass_notes = [
    (62, 1.5, 1.0),  # C# (chromatic approach to D)
    (64, 2.0, 1.0),  # D
    (65, 2.5, 1.0),  # E
    (67, 3.0, 1.0)   # F#
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (64, 1.5, 0.5),  # D
    (67, 1.5, 0.5),  # F#
    (72, 1.5, 0.5),  # A
    (62, 1.5, 0.5),  # C
    # Bar 3: Bm7 (B, D, F#, A)
    (69, 2.5, 0.5),  # B
    (64, 2.5, 0.5),  # D
    (67, 2.5, 0.5),  # F#
    (72, 2.5, 0.5),  # A
    # Bar 4: G7 (G, B, D, F)
    (67, 3.5, 0.5),  # G
    (69, 3.5, 0.5),  # B
    (64, 3.5, 0.5),  # D
    (62, 3.5, 0.5)   # F
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax: Melody - sparse, expressive, one short motif
# D (64) on beat 1, E (65) on beat 2, rest on beat 3, B (69) on beat 4
sax_notes = [
    (64, 1.5, 0.5),  # D on 1
    (65, 2.0, 0.5),  # E on 2
    (69, 3.5, 0.5)   # B on 4
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 1.0),  # Kick on 1
    (42, 3.0, 1.0),  # Hihat on 1
    (38, 3.5, 1.0),  # Snare on 2
    (42, 3.5, 1.0),  # Hihat on 2
    (36, 4.0, 1.0),  # Kick on 3
    (42, 4.0, 1.0),  # Hihat on 3
    (38, 4.5, 1.0),  # Snare on 4
    (42, 4.5, 1.0)   # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 3: Bass continues walking
bass_notes = [
    (67, 3.0, 1.0),  # F#
    (69, 3.5, 1.0),  # G
    (71, 4.0, 1.0),  # A
    (72, 4.5, 1.0)   # Bb
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Bar 3: Piano adds tension (Bm7)
piano_notes = [
    (69, 3.0, 0.5),  # B
    (64, 3.0, 0.5),  # D
    (67, 3.0, 0.5),  # F#
    (72, 3.0, 0.5),  # A
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 1.0),  # Kick on 1
    (42, 4.5, 1.0),  # Hihat on 1
    (38, 5.0, 1.0),  # Snare on 2
    (42, 5.0, 1.0),  # Hihat on 2
    (36, 5.5, 1.0),  # Kick on 3
    (42, 5.5, 1.0),  # Hihat on 3
    (38, 6.0, 1.0),  # Snare on 4
    (42, 6.0, 1.0)   # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Sax returns, finishes the motif
sax_notes = [
    (69, 4.5, 0.5)  # B on 1
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 4: Bass resolves
bass_notes = [
    (64, 4.5, 1.0)  # D
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Bar 4: Piano resolves to D7
piano_notes = [
    (64, 4.5, 0.5),  # D
    (67, 4.5, 0.5),  # F#
    (72, 4.5, 0.5),  # A
    (62, 4.5, 0.5)   # C
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
