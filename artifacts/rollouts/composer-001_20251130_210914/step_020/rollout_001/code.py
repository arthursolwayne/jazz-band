
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.9375, 0.1875), # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.3125, 0.1875), # Hihat on &3
    (38, 1.875, 0.375),  # Snare on 4
    (42, 2.0625, 0.1875) # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    (59, 1.5, 0.375),    # Bb (Fm7)
    (60, 1.875, 0.375),  # B (chromatic approach)
    (58, 2.25, 0.375),   # A (Fm7)
    (59, 2.625, 0.375),  # Bb (Fm7)
    (61, 2.875, 0.1875), # B (chromatic approach)
    (60, 3.125, 0.375),  # B (Fm7)
    (57, 3.5, 0.375),    # Ab (Fm7)
    (58, 3.875, 0.375),  # A (Fm7)
    (60, 4.25, 0.375),   # B (Fm7)
    (62, 4.625, 0.1875), # B (chromatic approach)
    (59, 4.875, 0.375),  # Bb (Fm7)
    (57, 5.25, 0.375),   # Ab (Fm7)
    (58, 5.625, 0.375),  # A (Fm7)
    (60, 6.0, 0.375)     # B (Fm7)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano chords - Diane
piano_notes = [
    # Bar 2
    (64, 1.5, 0.375),    # F (Fm7)
    (67, 1.5, 0.375),    # A
    (69, 1.5, 0.375),    # C
    (66, 1.5, 0.375),    # Bb
    (64, 2.25, 0.375),   # F (Fm7)
    (67, 2.25, 0.375),   # A
    (69, 2.25, 0.375),   # C
    (66, 2.25, 0.375),   # Bb
    # Bar 3
    (64, 3.0, 0.375),    # F (Fm7)
    (67, 3.0, 0.375),    # A
    (69, 3.0, 0.375),    # C
    (66, 3.0, 0.375),    # Bb
    (64, 3.75, 0.375),   # F (Fm7)
    (67, 3.75, 0.375),   # A
    (69, 3.75, 0.375),   # C
    (66, 3.75, 0.375),   # Bb
    # Bar 4
    (64, 4.5, 0.375),    # F (Fm7)
    (67, 4.5, 0.375),    # A
    (69, 4.5, 0.375),    # C
    (66, 4.5, 0.375),    # Bb
    (64, 5.25, 0.375),   # F (Fm7)
    (67, 5.25, 0.375),   # A
    (69, 5.25, 0.375),   # C
    (66, 5.25, 0.375)    # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax melody - Dante
sax_notes = [
    (62, 1.5, 0.375),    # G (Fm7)
    (64, 2.25, 0.375),   # A (Fm7)
    (62, 3.0, 0.375),    # G (Fm7)
    (60, 3.75, 0.375),   # F (Fm7)
    (62, 4.5, 0.375),    # G (Fm7)
    (64, 5.25, 0.375)    # A (Fm7)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums in Bars 2-4
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (38, 2.25, 0.375),   # Snare on 2
    (42, 2.4375, 0.1875), # Hihat on &2
    (36, 2.875, 0.375),  # Kick on 3
    (42, 3.0625, 0.1875), # Hihat on &3
    (38, 3.625, 0.375),  # Snare on 4
    (42, 3.8125, 0.1875), # Hihat on &4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (38, 5.25, 0.375),   # Snare on 2
    (42, 5.4375, 0.1875), # Hihat on &2
    (36, 5.875, 0.375),  # Kick on 3
    (42, 6.0625, 0.1875) # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
