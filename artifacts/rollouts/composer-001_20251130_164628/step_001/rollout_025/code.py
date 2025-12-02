
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
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    (65, 1.5), (66, 1.875), (64, 2.25), (63, 2.625),
    (65, 3.0), (66, 3.375), (64, 3.75), (63, 4.125),
    (65, 4.5), (66, 4.875), (64, 5.25), (63, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, comping in F
piano_notes = [
    # Bar 2
    (62, 1.875), (67, 1.875), (65, 1.875), (69, 1.875),  # F7
    (62, 2.625), (67, 2.625), (65, 2.625), (69, 2.625),  # F7
    # Bar 3
    (62, 3.375), (67, 3.375), (65, 3.375), (69, 3.375),  # F7
    (62, 4.125), (67, 4.125), (65, 4.125), (69, 4.125),  # F7
    # Bar 4
    (62, 4.875), (67, 4.875), (65, 4.875), (69, 4.875),  # F7
    (62, 5.625), (67, 5.625), (65, 5.625), (69, 5.625)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Saxophone: short motif, starts in bar 2
# F (65), G (67), E (64), F (65) — phrase starts on 2, ends on 4
sax_notes = [
    (67, 1.875), (64, 2.25), (65, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums continue for bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("waynes_moment.mid")
