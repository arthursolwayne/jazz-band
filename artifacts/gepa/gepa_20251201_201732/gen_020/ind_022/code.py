
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
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),   # D2 on 1
    (39, 1.875, 0.375), # Eb2 on 2
    (40, 2.25, 0.375),  # E2 on 3
    (42, 2.625, 0.375)  # G2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, resolving on the last bar
piano_notes = [
    # Bar 2: Dm7 (F, A, D, G)
    (62, 1.5, 0.375), (65, 1.5, 0.375), (67, 1.5, 0.375), (69, 1.5, 0.375), 
    # Bar 3: G7 (B, D, G, B)
    (71, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (71, 1.875, 0.375),
    # Bar 4: Cm7 (E, G, C, E)
    (64, 2.25, 0.375), (67, 2.25, 0.375), (60, 2.25, 0.375), (64, 2.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.1875),   # D4 on 1
    (66, 1.6875, 0.1875),# F4 on 2
    (67, 1.875, 0.1875), # G4 on 3
    (65, 2.0625, 0.1875),# E4 on 4
    (62, 2.25, 0.1875),  # D4 on 1
    (66, 2.4375, 0.1875),# F4 on 2
    (67, 2.625, 0.1875), # G4 on 3
    (65, 2.8125, 0.1875) # E4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    (38, 3.0, 0.375),   # D2 on 1
    (39, 3.375, 0.375), # Eb2 on 2
    (40, 3.75, 0.375),  # E2 on 3
    (42, 4.125, 0.375)  # G2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, resolving on the last bar
piano_notes = [
    # Bar 2: G7 (B, D, G, B)
    (71, 3.0, 0.375), (67, 3.0, 0.375), (69, 3.0, 0.375), (71, 3.0, 0.375), 
    # Bar 3: Cm7 (E, G, C, E)
    (64, 3.375, 0.375), (67, 3.375, 0.375), (60, 3.375, 0.375), (64, 3.375, 0.375),
    # Bar 4: Dm7 (F, A, D, G)
    (62, 3.75, 0.375), (65, 3.75, 0.375), (67, 3.75, 0.375), (69, 3.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    (38, 4.5, 0.375),   # D2 on 1
    (39, 4.875, 0.375), # Eb2 on 2
    (40, 5.25, 0.375),  # E2 on 3
    (42, 5.625, 0.375)  # G2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, resolving on the last bar
piano_notes = [
    # Bar 2: Cm7 (E, G, C, E)
    (64, 4.5, 0.375), (67, 4.5, 0.375), (60, 4.5, 0.375), (64, 4.5, 0.375),
    # Bar 3: Dm7 (F, A, D, G)
    (62, 4.875, 0.375), (65, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375),
    # Bar 4: Dm7 (F, A, D, G)
    (62, 5.25, 0.375), (65, 5.25, 0.375), (67, 5.25, 0.375), (69, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 4.5, 0.1875),   # D4 on 1
    (66, 4.6875, 0.1875),# F4 on 2
    (67, 4.875, 0.1875), # G4 on 3
    (65, 5.0625, 0.1875),# E4 on 4
    (62, 5.25, 0.1875),  # D4 on 1
    (66, 5.4375, 0.1875),# F4 on 2
    (67, 5.625, 0.1875), # G4 on 3
    (65, 5.8125, 0.1875) # E4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
