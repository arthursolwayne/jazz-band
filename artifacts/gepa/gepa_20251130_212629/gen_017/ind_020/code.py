
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
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (36, 1.5), (38, 1.75), (37, 2.0), (39, 2.25),
    (40, 2.5), (41, 2.75), (40, 3.0), (39, 3.25),
    (38, 3.5), (37, 3.75), (38, 4.0), (39, 4.25),
    (40, 4.5), (41, 4.75), (40, 5.0), (39, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.75), (64, 1.75), (67, 1.75), (69, 1.75),
    # Bar 3
    (62, 3.25), (64, 3.25), (67, 3.25), (69, 3.25),
    # Bar 4
    (62, 4.75), (64, 4.75), (67, 4.75), (69, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Saxophone - simple motif, emotionally charged
sax_notes = [
    (62, 1.5), (64, 1.75), (66, 2.0), (64, 2.25),
    (62, 2.5), (64, 2.75), (66, 3.0), (64, 3.25),
    (62, 3.5), (64, 3.75), (66, 4.0), (64, 4.25),
    (62, 4.5), (64, 4.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("jazz_intro.mid")
