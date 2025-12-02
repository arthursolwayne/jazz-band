
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
    (36, 0.0, 0.375),  # kick on 1
    (42, 0.0, 0.1875), # hihat on 1
    (38, 0.375, 0.375), # snare on 2
    (42, 0.375, 0.1875), # hihat on 2
    (36, 0.75, 0.375),  # kick on 3
    (42, 0.75, 0.1875), # hihat on 3
    (38, 1.125, 0.375), # snare on 4
    (42, 1.125, 0.1875) # hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), # D (1)
    (63, 1.875, 0.375), # Eb (2)
    (64, 2.25, 0.375), # E (3)
    (62, 2.625, 0.375), # D (4)
    (60, 3.0, 0.375), # C (1)
    (61, 3.375, 0.375), # C# (2)
    (62, 3.75, 0.375), # D (3)
    (60, 4.125, 0.375), # C (4)
    (62, 4.5, 0.375), # D (1)
    (63, 4.875, 0.375), # Eb (2)
    (64, 5.25, 0.375), # E (3)
    (62, 5.625, 0.375)  # D (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (62, 1.5, 0.375), # D
    (67, 1.5, 0.375), # F#
    (69, 1.5, 0.375), # A
    (60, 1.5, 0.375), # C
    # Bar 3: G7 (G, B, D, F)
    (67, 3.0, 0.375), # G
    (71, 3.0, 0.375), # B
    (69, 3.0, 0.375), # D
    (67, 3.0, 0.375), # F
    # Bar 4: C7 (C, E, G, B)
    (60, 4.5, 0.375), # C
    (64, 4.5, 0.375), # E
    (67, 4.5, 0.375), # G
    (71, 4.5, 0.375)  # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # kick on 1
    (42, 1.5, 0.1875), # hihat on 1
    (38, 1.875, 0.375), # snare on 2
    (42, 1.875, 0.1875), # hihat on 2
    (36, 2.25, 0.375),  # kick on 3
    (42, 2.25, 0.1875), # hihat on 3
    (38, 2.625, 0.375), # snare on 4
    (42, 2.625, 0.1875), # hihat on 4
    # Bar 3
    (36, 3.0, 0.375),  # kick on 1
    (42, 3.0, 0.1875), # hihat on 1
    (38, 3.375, 0.375), # snare on 2
    (42, 3.375, 0.1875), # hihat on 2
    (36, 3.75, 0.375),  # kick on 3
    (42, 3.75, 0.1875), # hihat on 3
    (38, 4.125, 0.375), # snare on 4
    (42, 4.125, 0.1875), # hihat on 4
    # Bar 4
    (36, 4.5, 0.375),  # kick on 1
    (42, 4.5, 0.1875), # hihat on 1
    (38, 4.875, 0.375), # snare on 2
    (42, 4.875, 0.1875), # hihat on 2
    (36, 5.25, 0.375),  # kick on 3
    (42, 5.25, 0.1875), # hihat on 3
    (38, 5.625, 0.375), # snare on 4
    (42, 5.625, 0.1875) # hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (67, 1.5, 0.375), # F# (1)
    (69, 1.875, 0.375), # A (2)
    (67, 2.25, 0.375), # F# (3)
    (69, 2.625, 0.375), # A (4)
    (67, 3.0, 0.375), # F# (1)
    (71, 3.375, 0.375), # B (2)
    (69, 3.75, 0.375), # A (3)
    (67, 4.125, 0.375), # F# (4)
    (69, 4.5, 0.375), # A (1)
    (71, 4.875, 0.375), # B (2)
    (69, 5.25, 0.375), # A (3)
    (67, 5.625, 0.375)  # F# (4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
