
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    (78, 1.5, 0.375),   # F2
    (84, 1.875, 0.375), # G2
    (82, 2.25, 0.375),  # F#2
    (78, 2.625, 0.375)  # F2
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: Open voicings, each bar a different chord
# Bar 2: Fmaj7 (F, A, C, E)
pn = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.0)
piano.notes.append(pn)

# Bar 3: Gm7 (G, Bb, D, F)
pn = pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.5)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.5)
piano.notes.append(pn)

# Bar 4: C7 (C, E, G, Bb)
pn = pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=3.0)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0)
piano.notes.append(pn)

# Dante: Motif - start on F, move to A, end on G (suspense)
sax_notes = [
    (71, 1.5, 0.375),   # F (bar 2, beat 1)
    (76, 2.0, 0.375),   # A (bar 2, beat 2)
    (77, 2.5, 0.375)    # G (bar 2, beat 3)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Drums (1.5 - 3.0s)
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Drums (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    (78, 3.0, 0.375),   # F2
    (84, 3.375, 0.375), # G2
    (82, 3.75, 0.375),  # F#2
    (78, 4.125, 0.375)  # F2
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: Open voicings, each bar a different chord
# Bar 4: C7 (C, E, G, Bb)
pn = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.5)
piano.notes.append(pn)
pn = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5)
piano.notes.append(pn)

# Dante: Motif - finish on C (resolution)
sax_notes = [
    (69, 3.0, 0.375)    # C (bar 4, beat 1)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
