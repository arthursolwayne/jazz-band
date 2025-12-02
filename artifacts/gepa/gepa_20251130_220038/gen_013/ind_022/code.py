
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
    (36, 0.0, 0.375),    # kick on 1
    (42, 0.0, 0.1875),   # hihat on 1
    (38, 0.375, 0.375),  # snare on 2
    (42, 0.375, 0.1875), # hihat on 2
    (36, 0.75, 0.375),   # kick on 3
    (42, 0.75, 0.1875),  # hihat on 3
    (38, 1.125, 0.375),  # snare on 4
    (42, 1.125, 0.1875)  # hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking in Fm
bass_notes = [
    # Bar 2
    (39, 1.5, 1.75),  # Fm root
    (40, 1.75, 2.0),  # Fm 9
    (38, 2.0, 2.25),  # Fm b7
    (37, 2.25, 2.5),  # Fm b6
    # Bar 3
    (39, 2.5, 2.75),  # Fm root
    (40, 2.75, 3.0),  # Fm 9
    (38, 3.0, 3.25),  # Fm b7
    (41, 3.25, 3.5),  # Fm b9
    # Bar 4
    (39, 3.5, 3.75),  # Fm root
    (40, 3.75, 4.0),  # Fm 9
    (38, 4.0, 4.25),  # Fm b7
    (37, 4.25, 4.5),  # Fm b6
    # Return to Fm root
    (39, 4.5, 4.75),  # Fm root
    (40, 4.75, 5.0),  # Fm 9
    (38, 5.0, 5.25),  # Fm b7
    (37, 5.25, 5.5),  # Fm b6
    (39, 5.5, 6.0)    # Fm root
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (42, 1.75, 2.0),  # Fm7 (F, Ab, C, D)
    (44, 1.75, 2.0),
    (47, 1.75, 2.0),
    (49, 1.75, 2.0),
    # Bar 3
    (42, 3.0, 3.25),  # Fm7
    (44, 3.0, 3.25),
    (47, 3.0, 3.25),
    (49, 3.0, 3.25),
    # Bar 4
    (42, 4.0, 4.25),  # Fm7
    (44, 4.0, 4.25),
    (47, 4.0, 4.25),
    (49, 4.0, 4.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Drums - continued
drum_notes = [
    (36, 1.5, 1.875),  # kick on 1
    (42, 1.5, 1.6875), # hihat on 1
    (38, 1.875, 2.125),  # snare on 2
    (42, 1.875, 2.0625), # hihat on 2
    (36, 2.25, 2.625),  # kick on 3
    (42, 2.25, 2.4375), # hihat on 3
    (38, 2.625, 2.875),  # snare on 4
    (42, 2.625, 2.8125), # hihat on 4
    (36, 3.0, 3.375),  # kick on 1
    (42, 3.0, 3.1875), # hihat on 1
    (38, 3.375, 3.625),  # snare on 2
    (42, 3.375, 3.5625), # hihat on 2
    (36, 3.75, 4.125),  # kick on 3
    (42, 3.75, 3.9375), # hihat on 3
    (38, 4.125, 4.375),  # snare on 4
    (42, 4.125, 4.3125), # hihat on 4
    (36, 4.5, 4.875),  # kick on 1
    (42, 4.5, 4.6875), # hihat on 1
    (38, 4.875, 5.125),  # snare on 2
    (42, 4.875, 5.0625), # hihat on 2
    (36, 5.25, 5.625),  # kick on 3
    (42, 5.25, 5.4375), # hihat on 3
    (38, 5.625, 5.875),  # snare on 4
    (42, 5.625, 5.8125)  # hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax - motif in Fm
# Start with a simple descending idea
sax_notes = [
    (42, 1.5, 1.75),    # Fm7
    (40, 1.75, 2.0),    # Ab
    (39, 2.0, 2.25),    # F
    (37, 2.25, 2.5),    # Eb
    # Leave it hanging...
    # Then return with a variation
    (42, 3.0, 3.25),    # F
    (39, 3.25, 3.5),    # F
    (37, 3.5, 3.75),    # Eb
    (36, 3.75, 4.0),    # D
    (40, 4.0, 4.25),    # Ab
    (39, 4.25, 4.5),    # F
    (42, 4.5, 4.75),    # F
    (40, 4.75, 5.0),    # Ab
    (42, 5.0, 5.25),    # F
    (39, 5.25, 5.5),    # F
    (37, 5.5, 5.75),    # Eb
    (36, 5.75, 6.0)     # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
