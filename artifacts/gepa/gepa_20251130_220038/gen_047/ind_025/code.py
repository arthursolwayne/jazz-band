
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (37, 1.5), (39, 1.875), (40, 2.25), (38, 2.625),
    (40, 3.0), (41, 3.375), (42, 3.75), (40, 4.125),
    (42, 4.5), (43, 4.875), (44, 5.25), (42, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Bb7 (F7 with flat 9)
    (62, 1.5), (67, 1.5), (69, 1.5), (60, 1.5),
    # Bar 3: C7
    (60, 3.0), (65, 3.0), (67, 3.0), (62, 3.0),
    # Bar 4: D7
    (62, 4.5), (67, 4.5), (69, 4.5), (64, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing
sax_notes = [
    (60, 1.5), (62, 1.625), (64, 1.75), (65, 1.875),  # F, G, A, A#
    (62, 2.0), (60, 2.125), (62, 2.25), (64, 2.375),  # G, F, G, A
    (65, 2.5), (64, 2.625), (62, 2.75), (60, 2.875),  # A, A, G, F
    (62, 3.0), (64, 3.125), (65, 3.25), (64, 3.375)   # G, A, A#, A
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Add the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
