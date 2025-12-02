
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D minor, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    # Bar 3
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125),
    # Bar 4
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp in D minor
piano_notes = [
    # Bar 2
    (62, 1.875), (67, 1.875), (64, 1.875), (69, 1.875),  # D7
    (62, 2.625), (67, 2.625), (64, 2.625), (69, 2.625),  # D7
    # Bar 3
    (62, 3.375), (67, 3.375), (64, 3.375), (69, 3.375),  # D7
    (62, 4.125), (67, 4.125), (64, 4.125), (69, 4.125),  # D7
    # Bar 4
    (62, 4.875), (67, 4.875), (64, 4.875), (69, 4.875),  # D7
    (62, 5.625), (67, 5.625), (64, 5.625), (69, 5.625)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Whisper at first, then a cry. Start with a short motif, leave it hanging
sax_notes = [
    # Bar 2
    (65, 1.5), (68, 1.75), (67, 2.0), (65, 2.0),  # Motif
    # Bar 3
    (65, 3.0), (68, 3.25), (67, 3.5), (65, 3.5),  # Repeat motif
    # Bar 4
    (65, 4.5), (68, 4.75), (67, 5.0), (69, 5.25), (71, 5.5), (69, 5.75)  # Cry
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.375), (42, 3.75), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.875), (42, 5.25), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
