
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add subtle dynamic variation
drum_notes = [
    (36, 0.0, 1.0),      # Kick on 1
    (42, 0.125, 0.25),   # Hihat on 1&
    (42, 0.375, 0.5),    # Hihat on 2&
    (38, 0.5, 0.75),     # Snare on 2
    (42, 0.625, 0.75),   # Hihat on 2&
    (42, 0.875, 1.0),    # Hihat on 3&
    (36, 1.0, 1.25),     # Kick on 3
    (42, 1.125, 1.25),   # Hihat on 3&
    (42, 1.375, 1.5),    # Hihat on 4&
    (38, 1.5, 1.75),     # Snare on 4
]
for note, start, end in drum_notes:
    drum_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif: concise, emotional, and memorable
# Dm7 -> G7 -> Cm7 -> F7 -> Dm7
# Start with D, leave it hanging
sax_notes = [
    (62, 1.5, 1.75),  # D4
    (67, 1.75, 2.0),  # G4
    (60, 2.0, 2.25),  # E4 (G7)
    (65, 2.25, 2.5),  # B4
    (59, 2.5, 2.75),  # D4 (Cm7)
    (62, 2.75, 3.0),  # F4
    (67, 3.0, 3.25),  # A4 (F7)
    (62, 3.25, 3.5),  # D4
    (67, 3.5, 3.75),  # G4
    (60, 3.75, 4.0),  # E4 (Dm7)
    (65, 4.0, 4.25),  # B4
    (59, 4.25, 4.5),  # D4
    (62, 4.5, 4.75),  # F4
    (67, 4.75, 5.0),  # A4
    (62, 5.0, 5.25),  # D4
    (67, 5.25, 5.5),  # G4
    (60, 5.5, 5.75),  # E4
    (65, 5.75, 6.0),  # B4
]
for note, start, end in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Bass line: active and melodic, not just walking
# Dm -> G7 -> Cm -> F7 -> Dm
# D - F - G - Bb - A - D - F - G - Bb - A - D - F - G - Bb - A - D
bass_notes = [
    (62, 1.5, 1.75),  # D4
    (67, 1.75, 2.0),  # F#4 (chromatic)
    (67, 2.0, 2.25),  # G4
    (69, 2.25, 2.5),  # Bb4
    (67, 2.5, 2.75),  # A4
    (62, 2.75, 3.0),  # D4
    (67, 3.0, 3.25),  # F#4
    (67, 3.25, 3.5),  # G4
    (69, 3.5, 3.75),  # Bb4
    (67, 3.75, 4.0),  # A4
    (62, 4.0, 4.25),  # D4
    (67, 4.25, 4.5),  # F#4
    (67, 4.5, 4.75),  # G4
    (69, 4.75, 5.0),  # Bb4
    (67, 5.0, 5.25),  # A4
    (62, 5.25, 5.5),  # D4
    (67, 5.5, 5.75),  # F#4
    (67, 5.75, 6.0),  # G4
]
for note, start, end in bass_notes:
    bass_note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano comping: 7th chords, on 2 and 4
# Dm7 (D, F, A, C), G7 (G, B, D, F), Cm7 (C, Eb, G, Bb), F7 (F, A, C, Eb)
# Left hand: root on 2 and 4
# Right hand: 7th chord on 2 and 4
# Dm7 on 2, G7 on 4, Cm7 on 2, F7 on 4
# Root motion: D - G - C - F

# Left hand (roots)
piano_notes_left = [
    (62, 1.75, 2.0),  # D4
    (67, 3.5, 4.0),   # G4
    (60, 4.25, 4.5),  # C4
    (64, 5.75, 6.0),  # F4
]

# Right hand (7th chords)
piano_notes_right = [
    # Dm7 at 1.75
    (62, 1.75, 2.0),  # D4
    (64, 1.75, 2.0),  # F4
    (67, 1.75, 2.0),  # A4
    (69, 1.75, 2.0),  # C5
    # G7 at 3.5
    (67, 3.5, 4.0),   # G4
    (71, 3.5, 4.0),   # B4
    (69, 3.5, 4.0),   # D5
    (71, 3.5, 4.0),   # F5
    # Cm7 at 4.25
    (60, 4.25, 4.5),  # C4
    (63, 4.25, 4.5),  # Eb4
    (67, 4.25, 4.5),  # G4
    (71, 4.25, 4.5),  # Bb4
    # F7 at 5.75
    (64, 5.75, 6.0),  # F4
    (67, 5.75, 6.0),  # A4
    (69, 5.75, 6.0),  # C5
    (71, 5.75, 6.0),  # Eb5
]
for note, start, end in piano_notes_left:
    piano_note = pretty_midi.Note(velocity=65, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)
for note, start, end in piano_notes_right:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

# Add dynamic variation to the piano
for note in piano.notes:
    if note.start < 1.75:
        note.velocity += 15
    elif note.start < 3.5:
        note.velocity -= 10
    elif note.start < 4.25:
        note.velocity += 10
    else:
        note.velocity -= 5

# Drums: 2-4 bars, full rhythm with dynamic variation
drum_notes = [
    # Bar 2
    (36, 1.5, 1.75),  # Kick on 1
    (38, 1.75, 2.0),  # Snare on 2
    (36, 2.0, 2.25),  # Kick on 3
    (38, 2.25, 2.5),  # Snare on 4
    # Bar 3
    (36, 2.5, 2.75),  # Kick on 1
    (38, 2.75, 3.0),  # Snare on 2
    (36, 3.0, 3.25),  # Kick on 3
    (38, 3.25, 3.5),  # Snare on 4
    # Bar 4
    (36, 3.5, 3.75),  # Kick on 1
    (38, 3.75, 4.0),  # Snare on 2
    (36, 4.0, 4.25),  # Kick on 3
    (38, 4.25, 4.5),  # Snare on 4
    # Hi-hats
    (42, 1.5, 1.625),  # Hihat on 1
    (42, 1.625, 1.75), # Hihat on 1&
    (42, 1.875, 2.0),  # Hihat on 2&
    (42, 2.125, 2.25), # Hihat on 3&
    (42, 2.375, 2.5),  # Hihat on 3&
    (42, 2.625, 2.75), # Hihat on 4&
    (42, 2.875, 3.0),  # Hihat on 1
    (42, 3.125, 3.25), # Hihat on 1&
    (42, 3.375, 3.5),  # Hihat on 2&
    (42, 3.625, 3.75), # Hihat on 3&
    (42, 3.875, 4.0),  # Hihat on 3&
    (42, 4.125, 4.25), # Hihat on 4&
    (42, 4.375, 4.5),  # Hihat on 1
    (42, 4.625, 4.75), # Hihat on 1&
    (42, 4.875, 5.0),  # Hihat on 2&
]
for note, start, end in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(drum_note)

# Add some dynamic variation to the drums
for note in drums.notes:
    if note.start < 1.75:
        note.velocity = 100
    elif note.start < 2.5:
        note.velocity = 90
    elif note.start < 3.5:
        note.velocity = 100
    elif note.start < 4.5:
        note.velocity = 90
    else:
        note.velocity = 100

# Add some rests to create space
# No rests needed in this arrangement

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
