
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
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.125, 0.25),  # Hihat on &1
    (42, 0.375, 0.5),   # Hihat on &2
    (38, 0.5, 1.0),     # Snare on 2
    (42, 0.625, 0.75),  # Hihat on &3
    (42, 0.875, 1.0),   # Hihat on &4
    (36, 1.0, 1.5),     # Kick on 3
    (42, 1.125, 1.25),  # Hihat on &3
    (42, 1.375, 1.5)    # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),   # F (root)
    (40, 1.875, 0.375),  # D (chromatic approach)
    (43, 2.25, 0.375),   # F (root)
    (46, 2.625, 0.375)   # A (fifth)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: open voicing, Fm7 (F, Ab, C, D), resolve on 4th beat
piano_notes = [
    (53, 1.5, 0.5),     # F (root)
    (60, 1.5, 0.5),     # C (third)
    (62, 1.5, 0.5),     # D (fifth)
    (57, 1.5, 0.5),     # Ab (seventh)

    (55, 2.0, 0.5),     # F (root)
    (60, 2.0, 0.5),     # C (third)
    (62, 2.0, 0.5),     # D (fifth)
    (58, 2.0, 0.5)      # G (chromatic approach)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - short motif, start it, leave it hanging
sax_notes = [
    (62, 1.5, 0.5),     # D (melody note)
    (65, 2.0, 0.5),     # F (melody note)
    (67, 2.5, 0.5),     # G (melody note)
    (65, 3.0, 0.5),     # F (melody note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Everyone in (3.0 - 4.5s)

# Bass: walking line, Ab (chromatic approach), G (fifth), Ab (chromatic approach), F (root)
bass_notes = [
    (40, 3.0, 0.375),   # Ab (chromatic)
    (46, 3.375, 0.375),  # G (fifth)
    (40, 3.75, 0.375),   # Ab (chromatic)
    (43, 4.125, 0.375)   # F (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: open voicing, Fm7 (F, Ab, C, D), resolve on 4th beat
piano_notes = [
    (53, 3.0, 0.5),     # F (root)
    (60, 3.0, 0.5),     # C (third)
    (62, 3.0, 0.5),     # D (fifth)
    (57, 3.0, 0.5),     # Ab (seventh)

    (55, 3.5, 0.5),     # F (root)
    (60, 3.5, 0.5),     # C (third)
    (62, 3.5, 0.5),     # D (fifth)
    (58, 3.5, 0.5)      # G (chromatic approach)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - continuation, build tension
sax_notes = [
    (62, 3.0, 0.5),     # D (melody note)
    (65, 3.5, 0.5),     # F (melody note)
    (67, 4.0, 0.5),     # G (melody note)
    (65, 4.5, 0.5),     # F (melody note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 1.0),     # Kick on 1
    (42, 3.125, 0.25),  # Hihat on &1
    (42, 3.375, 0.5),   # Hihat on &2
    (38, 3.5, 1.0),     # Snare on 2
    (42, 3.625, 0.25),  # Hihat on &3
    (42, 3.875, 1.0),   # Hihat on &4
    (36, 4.0, 1.0),     # Kick on 3
    (42, 4.125, 0.25),  # Hihat on &3
    (42, 4.375, 0.5),   # Hihat on &4
    (38, 4.5, 1.0),     # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Everyone in (4.5 - 6.0s)

# Bass: walking line, F (root), Ab (chromatic), G (fifth), F (root)
bass_notes = [
    (43, 4.5, 0.375),   # F (root)
    (40, 4.875, 0.375),  # Ab (chromatic)
    (46, 5.25, 0.375),   # G (fifth)
    (43, 5.625, 0.375)   # F (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: open voicing, Fm7 (F, Ab, C, D), resolve on 4th beat
piano_notes = [
    (53, 4.5, 0.5),     # F (root)
    (60, 4.5, 0.5),     # C (third)
    (62, 4.5, 0.5),     # D (fifth)
    (57, 4.5, 0.5),     # Ab (seventh)

    (55, 5.0, 0.5),     # F (root)
    (60, 5.0, 0.5),     # C (third)
    (62, 5.0, 0.5),     # D (fifth)
    (58, 5.0, 0.5)      # G (chromatic approach)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - finish the motif, resolve it
sax_notes = [
    (62, 4.5, 0.5),     # D (melody note)
    (65, 5.0, 0.5),     # F (melody note)
    (67, 5.5, 0.5),     # G (melody note)
    (64, 6.0, 0.5),     # E (resolution)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),     # Kick on 1
    (42, 4.625, 0.25),  # Hihat on &1
    (42, 4.875, 0.5),   # Hihat on &2
    (38, 5.0, 1.0),     # Snare on 2
    (42, 5.125, 0.25),  # Hihat on &3
    (42, 5.375, 0.5),   # Hihat on &4
    (36, 5.5, 1.0),     # Kick on 3
    (42, 5.625, 0.25),  # Hihat on &3
    (42, 5.875, 0.5),   # Hihat on &4
    (38, 6.0, 1.0),     # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
