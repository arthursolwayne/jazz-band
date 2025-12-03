
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on 1& 
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875),# Hihat on 2& 
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.9375, 0.1875),# Hihat on 3& 
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) - root, chromatic approach
bass_notes = [
    (38, 1.5, 0.375),    # D2 on 1
    (39, 1.875, 0.375),  # Eb2 on 2
    (38, 2.25, 0.375),   # D2 on 3
    (37, 2.625, 0.375)   # C2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, Dm7 (D F A C), resolve in bar 2
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (62, 1.5, 0.375),    # D4
    (65, 1.5, 0.375),    # F4
    (69, 1.5, 0.375),    # A4
    (72, 1.5, 0.375),    # C5
    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 2.25, 0.375),   # G4
    (71, 2.25, 0.375),   # Bb4
    (69, 2.25, 0.375),   # D4
    (65, 2.25, 0.375),   # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.0, 0.375),    # C4
    (64, 3.0, 0.375),    # Eb4
    (67, 3.0, 0.375),    # G4
    (71, 3.0, 0.375)     # Bb4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - D4, F4, Bb4, A4 (D F Bb A)
sax_notes = [
    (62, 1.5, 0.375),    # D4 on 1
    (65, 1.875, 0.375),  # F4 on 2
    (69, 2.25, 0.375),   # Bb4 on 3
    (68, 2.625, 0.375)   # A4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) - root, chromatic approach
bass_notes = [
    (38, 3.0, 0.375),    # D2 on 1
    (39, 3.375, 0.375),  # Eb2 on 2
    (38, 3.75, 0.375),   # D2 on 3
    (37, 4.125, 0.375)   # C2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, Gm7 (G, Bb, D, F), resolve in bar 3
piano_notes = [
    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 3.0, 0.375),    # G4
    (71, 3.0, 0.375),    # Bb4
    (69, 3.0, 0.375),    # D4
    (65, 3.0, 0.375),    # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.75, 0.375),   # C4
    (64, 3.75, 0.375),   # Eb4
    (67, 3.75, 0.375),   # G4
    (71, 3.75, 0.375)    # Bb4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.1875, 0.1875),# Hihat on 1& 
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.5625, 0.1875),# Hihat on 2& 
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.9375, 0.1875),# Hihat on 3& 
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.3125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) - root, chromatic approach
bass_notes = [
    (38, 4.5, 0.375),    # D2 on 1
    (39, 4.875, 0.375),  # Eb2 on 2
    (38, 5.25, 0.375),   # D2 on 3
    (37, 5.625, 0.375)   # C2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, Cm7 (C, Eb, G, Bb), resolve on the last
piano_notes = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 4.5, 0.375),    # C4
    (64, 4.5, 0.375),    # Eb4
    (67, 4.5, 0.375),    # G4
    (71, 4.5, 0.375)     # Bb4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - D4, F4, Bb4, A4, then repeat with a slight variation
sax_notes = [
    (62, 4.5, 0.375),    # D4 on 1
    (65, 4.875, 0.375),  # F4 on 2
    (69, 5.25, 0.375),   # Bb4 on 3
    (68, 5.625, 0.375)   # A4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.6875, 0.1875),# Hihat on 1& 
    (38, 4.875, 0.375),  # Snare on 2
    (42, 5.0625, 0.1875),# Hihat on 2& 
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.4375, 0.1875),# Hihat on 3& 
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.8125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
