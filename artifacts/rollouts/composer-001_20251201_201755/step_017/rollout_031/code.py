
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
    (42, 0.1875, 0.1875),  # Hihat on 1&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875),  # Hihat on 2&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.9375, 0.1875),  # Hihat on 3&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875)  # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D2 (root)
    (64, 1.875, 0.375),  # F#2 (fifth)
    (63, 2.25, 0.375),  # E2 (chromatic approach)
    (65, 2.625, 0.375),  # G2 (chromatic approach)
    (62, 2.625, 0.375),  # D2
    (64, 3.0, 0.375),  # F#2
    (63, 3.375, 0.375),  # E2
    (65, 3.75, 0.375),  # G2
    (62, 3.75, 0.375),  # D2
    (64, 4.125, 0.375),  # F#2
    (63, 4.5, 0.375),  # E2
    (65, 4.875, 0.375)   # G2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # A
    (64, 1.5, 0.375),  # F#
    (66, 1.5, 0.375),  # C#
    # Bar 3: Bm7 (B, D, F#, A)
    (69, 2.25, 0.375),  # B
    (71, 2.25, 0.375),  # D
    (67, 2.25, 0.375),  # F#
    (72, 2.25, 0.375),  # A
    # Bar 4: G7 (G, B, D, F)
    (67, 3.0, 0.375),  # G
    (71, 3.0, 0.375),  # B
    (69, 3.0, 0.375),  # D
    (65, 3.0, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante): motif, start it, leave it hanging, finish it
# Motif: D (62), F (65), G (67), D (62) — short and singable
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (67, 2.25, 0.375),  # G
    (62, 2.625, 0.375),  # D
    (62, 3.0, 0.375),  # D (reprise)
    (65, 3.375, 0.375),  # F
    (67, 3.75, 0.375),  # G
    (62, 4.125, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
