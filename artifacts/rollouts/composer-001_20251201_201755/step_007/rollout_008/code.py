
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
    (42, 0.125, 0.25), # Hihat on 1&
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.5, 0.25),   # Hihat on 2&
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.875, 0.25), # Hihat on 3&
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.25, 0.25)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
# Bar 2: G (D2) -> F (C2) -> E (B2) -> D (F2)
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (40, 1.875, 0.375), # F2 on 2
    (43, 2.25, 0.375),  # B2 on 3
    (42, 2.625, 0.375), # A2 on 4
    (38, 2.875, 0.375), # D2 on 1
    (40, 3.25, 0.375),  # F2 on 2
    (43, 3.625, 0.375), # B2 on 3
    (42, 4.0, 0.375),   # A2 on 4
    (38, 4.25, 0.375),  # D2 on 1
    (40, 4.625, 0.375), # F2 on 2
    (43, 5.0, 0.375),   # B2 on 3
    (42, 5.375, 0.375)  # A2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: F7 (F A C E)
piano_notes = [
    (65, 1.5, 0.375), # F4
    (68, 1.5, 0.375), # A4
    (69, 1.5, 0.375), # Bb4
    (72, 1.5, 0.375), # C5
    (67, 1.5, 0.375), # G4
    (72, 1.5, 0.375), # C5
    (76, 1.5, 0.375), # E5
    (65, 1.5, 0.375), # F4

    # Bar 3: Bb7 (Bb D F A)
    (62, 2.25, 0.375), # Bb4
    (65, 2.25, 0.375), # D4
    (67, 2.25, 0.375), # F4
    (69, 2.25, 0.375), # A4
    (62, 2.25, 0.375), # Bb4
    (65, 2.25, 0.375), # D4
    (69, 2.25, 0.375), # A4
    (62, 2.25, 0.375), # Bb4

    # Bar 4: D7 (D F# A C)
    (62, 3.0, 0.375),  # D4
    (66, 3.0, 0.375),  # F#4
    (69, 3.0, 0.375),  # A4
    (72, 3.0, 0.375),  # C5
    (62, 3.0, 0.375),  # D4
    (66, 3.0, 0.375),  # F#4
    (69, 3.0, 0.375),  # A4
    (72, 3.0, 0.375),  # C5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.625, 0.25), # Hihat on 1&
    (38, 1.875, 0.375),# Snare on 2
    (42, 2.0, 0.25),   # Hihat on 2&
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.375, 0.25), # Hihat on 3&
    (38, 2.625, 0.375),# Snare on 4
    (42, 2.75, 0.25),  # Hihat on 4&
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.125, 0.25), # Hihat on 1&
    (38, 3.375, 0.375),# Snare on 2
    (42, 3.5, 0.25),   # Hihat on 2&
    (36, 3.75, 0.375), # Kick on 3
    (42, 3.875, 0.25), # Hihat on 3&
    (38, 4.125, 0.375),# Snare on 4
    (42, 4.25, 0.25),  # Hihat on 4&
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.625, 0.25), # Hihat on 1&
    (38, 4.875, 0.375),# Snare on 2
    (42, 5.0, 0.25),   # Hihat on 2&
    (36, 5.25, 0.375), # Kick on 3
    (42, 5.375, 0.25), # Hihat on 3&
    (38, 5.625, 0.375),# Snare on 4
    (42, 5.75, 0.25)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Melody: F G Ab Bb (Bar 2) -> D (Bar 3) -> F (Bar 4)
sax_notes = [
    (65, 1.5, 0.375),  # F4
    (66, 1.875, 0.375), # G4
    (67, 2.25, 0.375),  # Ab4
    (69, 2.625, 0.375), # Bb4
    (62, 3.0, 0.375),   # D4
    (65, 3.375, 0.375), # F4
    (65, 3.75, 0.375),  # F4
    (66, 4.125, 0.375), # G4
    (67, 4.5, 0.375),   # Ab4
    (69, 4.875, 0.375), # Bb4
    (65, 5.25, 0.375),  # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
