
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (bass): Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    # Bar 3
    (64, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4
    (63, 4.5, 0.375), (62, 4.875, 0.375), (60, 5.25, 0.375), (62, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane (piano): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (79, 1.875, 0.1875), (76, 1.875, 0.1875), (74, 1.875, 0.1875), (71, 1.875, 0.1875),
    # Bar 3
    (79, 3.375, 0.1875), (76, 3.375, 0.1875), (74, 3.375, 0.1875), (71, 3.375, 0.1875),
    # Bar 4
    (79, 4.875, 0.1875), (76, 4.875, 0.1875), (74, 4.875, 0.1875), (71, 4.875, 0.1875)
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start motif (C# - D - B - C)
sax_notes = [
    (63, 1.5, 0.375), (64, 1.875, 0.375), (61, 2.25, 0.375), (62, 2.625, 0.375),
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (C# - D - B - C)
    (63, 4.5, 0.375), (64, 4.875, 0.375), (61, 5.25, 0.375), (62, 5.625, 0.375)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
