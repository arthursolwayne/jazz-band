
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Marcus - walking line in F
bass_notes = [
    (38, 1.5, 0.375),  # D2
    (43, 1.875, 0.375),  # G2
    (38, 2.25, 0.375),  # D2
    (40, 2.625, 0.375),  # F2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane - open voicings, each bar a different chord
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    (53, 1.5, 0.375),
    (60, 1.5, 0.375),
    (65, 1.5, 0.375),
    (67, 1.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante - motif starts
sax_notes = [
    (64, 1.5, 0.375),  # F
    (66, 1.875, 0.375),  # G
    (64, 2.25, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Marcus - walking line in F
bass_notes = [
    (38, 3.0, 0.375),  # D2
    (43, 3.375, 0.375),  # G2
    (38, 3.75, 0.375),  # D2
    (40, 4.125, 0.375),  # F2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane - open voicings, each bar a different chord
# Bar 3: Dm7 (D F A C)
piano_notes = [
    (50, 3.0, 0.375),
    (52, 3.0, 0.375),
    (57, 3.0, 0.375),
    (60, 3.0, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante - motif continues
sax_notes = [
    (62, 3.0, 0.375),  # E
    (64, 3.375, 0.375),  # F
    (62, 3.75, 0.375),  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Marcus - walking line in F
bass_notes = [
    (38, 4.5, 0.375),  # D2
    (43, 4.875, 0.375),  # G2
    (38, 5.25, 0.375),  # D2
    (40, 5.625, 0.375),  # F2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane - open voicings, each bar a different chord
# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    (60, 4.5, 0.375),
    (63, 4.5, 0.375),
    (67, 4.5, 0.375),
    (68, 4.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante - motif resolves
sax_notes = [
    (62, 4.5, 0.375),  # E
    (64, 4.875, 0.375),  # F (resolve)
    (62, 5.25, 0.375),  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
