
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (38, 0.75, 0.375),    # Snare on 2
    (42, 0.9375, 0.1875), # Hihat on &2
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.3125, 0.1875), # Hihat on &3
    (38, 1.875, 0.375),   # Snare on 4
    (42, 2.0625, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F
bass_notes = [
    (45, 1.5, 0.375),     # F3 - 1
    (46, 1.875, 0.375),   # G3 - 2
    (47, 2.25, 0.375),    # Ab3 - 3
    (48, 2.625, 0.375),   # Bb3 - 4
    (48, 3.0, 0.375),     # Bb3 - 1
    (47, 3.375, 0.375),   # Ab3 - 2
    (46, 3.75, 0.375),    # G3 - 3
    (45, 4.125, 0.375),   # F3 - 4
    (45, 4.5, 0.375),     # F3 - 1
    (46, 4.875, 0.375),   # G3 - 2
    (47, 5.25, 0.375),    # Ab3 - 3
    (48, 5.625, 0.375)    # Bb3 - 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 & 4, comp
piano_notes = [
    # Bar 2
    (53, 1.875, 0.1875),  # B7 - 2
    (50, 1.875, 0.1875),
    (52, 1.875, 0.1875),
    (55, 1.875, 0.1875),
    (53, 2.625, 0.1875),  # B7 - 4
    (50, 2.625, 0.1875),
    (52, 2.625, 0.1875),
    (55, 2.625, 0.1875),
    # Bar 3
    (53, 3.375, 0.1875),  # B7 - 2
    (50, 3.375, 0.1875),
    (52, 3.375, 0.1875),
    (55, 3.375, 0.1875),
    (53, 4.125, 0.1875),  # B7 - 4
    (50, 4.125, 0.1875),
    (52, 4.125, 0.1875),
    (55, 4.125, 0.1875),
    # Bar 4
    (53, 4.875, 0.1875),  # B7 - 2
    (50, 4.875, 0.1875),
    (52, 4.875, 0.1875),
    (55, 4.875, 0.1875),
    (53, 5.625, 0.1875),  # B7 - 4
    (50, 5.625, 0.1875),
    (52, 5.625, 0.1875),
    (55, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - full kit
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (38, 2.25, 0.375),    # Snare on 2
    (42, 2.4375, 0.1875), # Hihat on &2
    (36, 2.625, 0.375),   # Kick on 3
    (42, 2.8125, 0.1875), # Hihat on &3
    (38, 3.375, 0.375),   # Snare on 4
    (42, 3.5625, 0.1875), # Hihat on &4
    (36, 3.75, 0.375),    # Kick on 1
    (42, 3.9375, 0.1875), # Hihat on &1
    (38, 4.5, 0.375),     # Snare on 2
    (42, 4.6875, 0.1875), # Hihat on &2
    (36, 4.875, 0.375),   # Kick on 3
    (42, 5.0625, 0.1875), # Hihat on &3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.8125, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante) - short motif, make it sing
sax_notes = [
    (62, 1.5, 0.6),     # D4 - start
    (66, 2.1, 0.6),     # G4 - end first phrase
    (60, 2.7, 0.6),     # C4
    (62, 3.3, 0.6),     # D4
    (64, 3.9, 0.6),     # E4
    (62, 4.5, 0.6),     # D4
    (60, 5.1, 0.6),     # C4
    (62, 5.7, 0.6)      # D4 - end
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_russo_intro.mid')
