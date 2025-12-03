
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

# Drums - Bar 1
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.75, 0.125),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hihat on &3
    (38, 1.5, 0.375)     # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass Line (Walking line, roots and fifths)
bass_notes = [
    (38, 1.5, 0.375),  # F (root)
    (40, 1.875, 0.375),  # G (fifth)
    (39, 2.25, 0.375),  # F# (chromatic approach)
    (38, 2.625, 0.375),  # F (root)
    (43, 2.625, 0.375),  # C (fifth of Bb)
    (41, 2.625, 0.375),  # Bb (chromatic approach)
    (43, 3.0, 0.375),  # C (resolve)
    (45, 3.375, 0.375),  # D (fifth of G)
    (44, 3.75, 0.375),  # C# (chromatic approach)
    (45, 4.125, 0.375),  # D (fifth of G)
    (47, 4.5, 0.375),  # E (fifth of A)
    (46, 4.875, 0.375),  # D# (chromatic approach)
    (47, 5.25, 0.375),  # E (fifth of A)
    (50, 5.625, 0.375)   # F (root of F)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Diane - Piano (Open voicings, different chord each bar)
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    (62, 1.5, 0.375),  # F
    (66, 1.5, 0.375),  # A
    (69, 1.5, 0.375),  # C
    (72, 1.5, 0.375),  # E
    (65, 1.875, 0.375)  # A (comp on 2)
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Bar 3: Bbmaj7 (Bb D F A)
piano_notes = [
    (59, 2.25, 0.375),  # Bb
    (62, 2.25, 0.375),  # D
    (64, 2.25, 0.375),  # F
    (67, 2.25, 0.375),  # A
    (66, 2.625, 0.375)  # A (comp on 3)
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Bar 4: G7 (G B D F)
piano_notes = [
    (67, 3.0, 0.375),  # G
    (71, 3.0, 0.375),  # B
    (69, 3.0, 0.375),  # D
    (67, 3.0, 0.375),  # F (diminished)
    (67, 3.375, 0.375),  # G (comp on 4)
    (71, 3.375, 0.375)  # B
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Little Ray - Drums (Bars 2-4)
# Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.125),  # Hihat on &1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hihat on &2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.125),  # Hihat on &3
    (38, 2.625, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat on &1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on &2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.125),  # Hihat on &3
    (38, 4.125, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat on &1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on &2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.125),  # Hihat on &3
    (38, 5.625, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Dante - Sax (Bars 2-4)
# Motif: F -> Bb -> C -> F (start on 2, end on 4)
sax_notes = [
    (65, 1.875, 0.375),  # Bb (start)
    (69, 2.25, 0.375),  # C
    (65, 2.625, 0.375),  # Bb
    (69, 3.0, 0.375),  # C
    (65, 3.375, 0.375),  # Bb (reprise)
    (69, 3.75, 0.375),  # C
    (77, 4.125, 0.375),  # F (resolve)
    (69, 4.5, 0.375),  # C (end)
    (65, 4.875, 0.375)  # Bb (end)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
