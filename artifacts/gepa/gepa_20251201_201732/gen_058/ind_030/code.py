
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (38, 0.5, 0.375),     # Snare on 2
    (42, 0.6875, 0.1875), # Hihat on &2
    (36, 0.875, 0.375),   # Kick on 3
    (42, 0.96875, 0.1875),# Hihat on &3
    (38, 1.25, 0.375),    # Snare on 4
    (42, 1.4375, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),     # D2 on 1
    (40, 1.875, 0.375),   # F2 on 2
    (42, 2.25, 0.375),    # A2 on 3
    (38, 2.625, 0.375),   # D2 on 4
    (43, 2.625, 0.375),   # D#2 on 4 (chromatic approach)
    (38, 3.0, 0.375),     # D2 on 1
    (40, 3.375, 0.375),   # F2 on 2
    (42, 3.75, 0.375),    # A2 on 3
    (38, 4.125, 0.375),   # D2 on 4
    (43, 4.125, 0.375),   # D#2 on 4
    (38, 4.5, 0.375),     # D2 on 1
    (40, 4.875, 0.375),   # F2 on 2
    (42, 5.25, 0.375),    # A2 on 3
    (38, 5.625, 0.375)    # D2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (62, 1.5, 0.5),  # D4
    (65, 1.5, 0.5),  # F4
    (67, 1.5, 0.5),  # A4
    (69, 1.5, 0.5),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    (67, 2.25, 0.5),  # G4
    (71, 2.25, 0.5),  # B4
    (69, 2.25, 0.5),  # D4
    (65, 2.25, 0.5),  # F4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    (60, 3.0, 0.5),   # C4
    (63, 3.0, 0.5),   # Eb4
    (67, 3.0, 0.5),   # G4
    (62, 3.0, 0.5),   # Bb4
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: D4 - F4 - G4 - D4 (1.5s), then return at 4.5s
sax_notes = [
    (62, 1.5, 0.375),  # D4 on 1
    (65, 1.875, 0.375), # F4 on 2
    (67, 2.25, 0.375),  # G4 on 3
    (62, 2.625, 0.375), # D4 on 4
    (62, 4.5, 0.375),   # D4 on 1 (repeat)
    (65, 4.875, 0.375), # F4 on 2
    (67, 5.25, 0.375),  # G4 on 3
    (62, 5.625, 0.375)  # D4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_bar = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_bar, end=start_bar + 0.375))
    # Hihat on &1
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start_bar + 0.1875, end=start_bar + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_bar + 0.5, end=start_bar + 0.875))
    # Hihat on &2
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start_bar + 0.6875, end=start_bar + 0.6875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_bar + 0.875, end=start_bar + 1.25))
    # Hihat on &3
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start_bar + 0.96875, end=start_bar + 0.96875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_bar + 1.25, end=start_bar + 1.625))
    # Hihat on &4
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start_bar + 1.4375, end=start_bar + 1.4375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
