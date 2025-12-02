
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
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53), walking line with chromatic approach
bass_notes = [
    (53, 1.5, 0.375),  # F2 on 1
    (52, 1.875, 0.375),  # Eb2 on 2
    (54, 2.25, 0.375),  # G2 on 3
    (53, 2.625, 0.375)  # F2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, each bar a different chord
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5, 0.375),  # F
    (76, 1.5, 0.375),  # A
    (69, 1.5, 0.375),  # C
    (74, 1.5, 0.375),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (62, 2.25, 0.375),  # Bb
    (67, 2.25, 0.375),  # D
    (69, 2.25, 0.375),  # F
    (64, 2.25, 0.375),  # Ab
    # Bar 4: Dm7 (D, F, A, C)
    (67, 2.625, 0.375),  # D
    (69, 2.625, 0.375),  # F
    (76, 2.625, 0.375),  # A
    (69, 2.625, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody starts in bar 2, one motif
# F - G - Bb - F (starts on 2, ends on 4)
sax_notes = [
    (65, 1.875, 0.375),  # G on 2
    (69, 2.25, 0.375),   # Bb on 3
    (65, 2.625, 0.375)   # F on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approach
bass_notes = [
    (53, 3.0, 0.375),  # F2 on 1
    (52, 3.375, 0.375),  # Eb2 on 2
    (54, 3.75, 0.375),  # G2 on 3
    (53, 4.125, 0.375)  # F2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, each bar a different chord
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (62, 3.0, 0.375),  # Bb
    (67, 3.0, 0.375),  # D
    (69, 3.0, 0.375),  # F
    (64, 3.0, 0.375),  # Ab
    # Bar 4: Dm7 (D, F, A, C)
    (67, 3.75, 0.375),  # D
    (69, 3.75, 0.375),  # F
    (76, 3.75, 0.375),  # A
    (69, 3.75, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif continuation, leave it hanging
sax_notes = [
    (67, 3.375, 0.375),  # A on 2
    (69, 3.75, 0.375),   # Bb on 3
    (65, 4.125, 0.375)   # F on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approach
bass_notes = [
    (53, 4.5, 0.375),  # F2 on 1
    (52, 4.875, 0.375),  # Eb2 on 2
    (54, 5.25, 0.375),  # G2 on 3
    (53, 5.625, 0.375)  # F2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, each bar a different chord
# Bar 4: Dm7 (D, F, A, C)
piano_notes = [
    (67, 4.5, 0.375),  # D
    (69, 4.5, 0.375),  # F
    (76, 4.5, 0.375),  # A
    (69, 4.5, 0.375),  # C
    # Bar 4 resolution: Fmaj7 (F, A, C, E)
    (65, 5.625, 0.375),  # F
    (76, 5.625, 0.375),  # A
    (69, 5.625, 0.375),  # C
    (74, 5.625, 0.375)   # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif resolution on bar 4
sax_notes = [
    (67, 4.875, 0.375),  # D on 2
    (65, 5.25, 0.375),   # F on 3
    (65, 5.625, 0.375)   # F on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Full bar (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo_intro.mid')
