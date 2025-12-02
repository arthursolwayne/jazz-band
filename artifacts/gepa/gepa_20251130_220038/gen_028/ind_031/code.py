
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
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (37, 1.5), (38, 1.875), (39, 2.25), (40, 2.625),
    (41, 3.0), (42, 3.375), (43, 3.75), (44, 4.125),
    (45, 4.5), (46, 4.875), (47, 5.25), (48, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875), (64, 1.875), (67, 1.875),  # F7
    (65, 2.625), (67, 2.625), (70, 2.625),  # Bb7
    # Bar 3
    (69, 3.375), (71, 3.375), (74, 3.375),  # E7
    (72, 4.125), (74, 4.125), (77, 4.125),  # A7
    # Bar 4
    (62, 4.875), (64, 4.875), (67, 4.875),  # F7
    (65, 5.625), (67, 5.625), (70, 5.625)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Dante: One short motif, make it sing. Whisper then cry
sax_notes = [
    (66, 1.5), (68, 1.75), (67, 2.0), (66, 2.25),  # Whisper
    (68, 2.5), (71, 2.75), (72, 3.0), (71, 3.25),  # Build
    (72, 3.5), (70, 3.75), (68, 4.0), (66, 4.25),  # Cry
    (65, 4.5), (67, 4.75), (68, 5.0), (67, 5.25),  # Resolve
    (66, 5.5), (64, 5.75)                         # Echo
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_at_cellar.mid")
