
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Set the start time for the next section
start_time = 1.5

# Marcus: Walking bass line in Dm, chromatic approaches
bass_notes = [
    (62, start_time),      # D
    (60, start_time + 0.375), # Bb
    (62, start_time + 0.75),  # D
    (64, start_time + 1.125), # F
    (62, start_time + 1.5),   # D
    (60, start_time + 1.875), # Bb
    (62, start_time + 2.25),  # D
    (64, start_time + 2.625), # F
    (62, start_time + 3.0),   # D
    (60, start_time + 3.375), # Bb
    (62, start_time + 3.75),  # D
    (64, start_time + 4.125), # F
    (62, start_time + 4.5),   # D
    (60, start_time + 4.875), # Bb
    (62, start_time + 5.25),  # D
    (64, start_time + 5.625)  # F
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# F7 = F, A, C, E
# Bbm7 = Bb, D, F, Ab
# G7 = G, B, D, F
piano_notes = [
    (62, start_time + 0.375), (65, start_time + 0.375), (67, start_time + 0.375), (60, start_time + 0.375),  # Dm7 on 2
    (62, start_time + 1.5), (65, start_time + 1.5), (67, start_time + 1.5), (60, start_time + 1.5),        # Dm7 on 2
    (65, start_time + 2.625), (67, start_time + 2.625), (69, start_time + 2.625), (62, start_time + 2.625), # F7 on 4
    (62, start_time + 3.75), (65, start_time + 3.75), (67, start_time + 3.75), (60, start_time + 3.75),    # Dm7 on 2
    (62, start_time + 5.25), (65, start_time + 5.25), (67, start_time + 5.25), (60, start_time + 5.25)     # Dm7 on 2
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, start_time), (38, start_time + 0.375), (42, start_time + 0.375),
    (36, start_time + 1.125), (38, start_time + 1.5), (42, start_time + 1.5),
    (36, start_time + 2.625), (38, start_time + 3.0), (42, start_time + 3.0),
    (36, start_time + 3.75), (38, start_time + 4.125), (42, start_time + 4.125),
    (36, start_time + 5.25), (38, start_time + 5.625), (42, start_time + 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, one short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Bb, F, D (with some chromaticism)
sax_notes = [
    (62, start_time),          # D
    (60, start_time + 0.375),  # Bb
    (64, start_time + 0.75),   # F
    (62, start_time + 1.125),  # D
    (62, start_time + 2.25),   # D (return)
    (60, start_time + 2.625),  # Bb
    (64, start_time + 3.0),    # F
    (62, start_time + 3.375),  # D
    (62, start_time + 4.5),    # D (return)
    (60, start_time + 4.875),  # Bb
    (64, start_time + 5.25),   # F
    (62, start_time + 5.625)   # D
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
