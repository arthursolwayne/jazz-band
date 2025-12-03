
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
    (42, 0.1875, 0.1875), # Hihat on 1&
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.5625, 0.1875), # Hihat on 2&
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.9375, 0.1875), # Hihat on 3&
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.3125, 0.1875)  # Hihat on 4&
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Dm
bass_notes = [
    (43, 1.5, 1.5),   # D2 (root)
    (40, 1.875, 1.875), # F (fifth)
    (39, 2.25, 2.25), # Eb (chromatic approach)
    (43, 2.625, 2.625), # D2 (root)
    (43, 2.625, 2.625), # D2 (root)
    (40, 3.0, 3.0), # F (fifth)
    (39, 3.375, 3.375), # Eb (chromatic approach)
    (43, 3.75, 3.75), # D2 (root)
    (43, 3.75, 3.75), # D2 (root)
    (40, 4.125, 4.125), # F (fifth)
    (39, 4.5, 4.5), # Eb (chromatic approach)
    (43, 4.875, 4.875), # D2 (root)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Diane - Piano, open voicings, resolve on the last chord of each bar
# Bar 2: Dm7
piano_notes = [
    (62, 1.5, 1.5), # D4
    (67, 1.5, 1.5), # G4
    (69, 1.5, 1.5), # A4
    (72, 1.5, 1.5), # C5
]
# Bar 3: G7
piano_notes.extend([
    (67, 2.25, 2.25), # G4
    (71, 2.25, 2.25), # B4
    (72, 2.25, 2.25), # C5
    (76, 2.25, 2.25), # E5
])
# Bar 4: Cm7
piano_notes.extend([
    (60, 3.0, 3.0), # C4
    (65, 3.0, 3.0), # E4
    (67, 3.0, 3.0), # G4
    (72, 3.0, 3.0), # C5
])
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray - Drums in bars 2-4
drum_notes = [
    (36, 1.5, 1.5),   # Kick on 1
    (42, 1.6875, 0.1875), # Hihat on 1&
    (38, 1.875, 1.875),   # Snare on 2
    (42, 2.0625, 0.1875), # Hihat on 2&
    (36, 2.25, 1.5),    # Kick on 3
    (42, 2.4375, 0.1875), # Hihat on 3&
    (38, 2.625, 1.875),   # Snare on 4
    (42, 2.8125, 0.1875), # Hihat on 4&
    (36, 3.0, 1.5),    # Kick on 1
    (42, 3.1875, 0.1875), # Hihat on 1&
    (38, 3.375, 1.875),   # Snare on 2
    (42, 3.5625, 0.1875), # Hihat on 2&
    (36, 3.75, 1.5),    # Kick on 3
    (42, 3.9375, 0.1875), # Hihat on 3&
    (38, 4.125, 1.875),   # Snare on 4
    (42, 4.3125, 0.1875), # Hihat on 4&
    (36, 4.5, 1.5),    # Kick on 1
    (42, 4.6875, 0.1875), # Hihat on 1&
    (38, 4.875, 1.875),   # Snare on 2
    (42, 5.0625, 0.1875), # Hihat on 2&
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante - Saxophone Motif (Bar 2, first 2 notes)
# Dm7: D4, F4, A4, C5 -> motif: D4 -> F4 -> A4 -> D4 (hanging)
sax_notes = [
    (62, 1.5, 1.5), # D4
    (67, 1.875, 1.875), # F4
    (69, 2.25, 2.25), # A4
    (62, 2.625, 2.625), # D4
    # Return to motif in Bar 4
    (62, 4.5, 4.5), # D4
    (67, 4.875, 4.875), # F4
    (69, 5.25, 5.25), # A4
    (62, 5.625, 5.625) # D4
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
