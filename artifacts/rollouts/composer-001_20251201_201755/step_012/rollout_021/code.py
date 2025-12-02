
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
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375), # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (42, 2.625, 0.375), # F2 (chromatic approach)
    (38, 3.0, 0.375),   # D2 (root)
    (40, 3.375, 0.375), # Eb2 (chromatic approach)
    (43, 3.75, 0.375),  # G2 (fifth)
    (42, 4.125, 0.375), # F2 (chromatic approach)
    (38, 4.5, 0.375),   # D2 (root)
    (40, 4.875, 0.375), # Eb2 (chromatic approach)
    (43, 5.25, 0.375),  # G2 (fifth)
    (42, 5.625, 0.375)  # F2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (62, 1.5, 0.1875), # D4
    (64, 1.5, 0.1875), # F4
    (67, 1.5, 0.1875), # A4
    (69, 1.5, 0.1875), # C5
    (62, 1.6875, 0.1875), # D4
    (64, 1.6875, 0.1875), # F4
    (67, 1.6875, 0.1875), # A4
    (69, 1.6875, 0.1875), # C5
]
# Bar 3: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    (60, 2.25, 0.1875), # C4
    (62, 2.25, 0.1875), # Eb4
    (65, 2.25, 0.1875), # G4
    (67, 2.25, 0.1875), # Bb4
    (60, 2.4375, 0.1875), # C4
    (62, 2.4375, 0.1875), # Eb4
    (65, 2.4375, 0.1875), # G4
    (67, 2.4375, 0.1875), # Bb4
])
# Bar 4: G7 (G-B-D-F)
piano_notes.extend([
    (67, 3.0, 0.1875), # G4
    (69, 3.0, 0.1875), # B4
    (71, 3.0, 0.1875), # D5
    (73, 3.0, 0.1875), # F5
    (67, 3.1875, 0.1875), # G4
    (69, 3.1875, 0.1875), # B4
    (71, 3.1875, 0.1875), # D5
    (73, 3.1875, 0.1875), # F5
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - E4 - F4 - D4 (sax melody)
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (64, 1.875, 0.375), # E4
    (65, 2.25, 0.375),  # F4
    (62, 2.625, 0.375), # D4
    (62, 3.0, 0.375),   # D4
    (64, 3.375, 0.375), # E4
    (65, 3.75, 0.375),  # F4
    (62, 4.125, 0.375)  # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("cellar_intro.mid")
