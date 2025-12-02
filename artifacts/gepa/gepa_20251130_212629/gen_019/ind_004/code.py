
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

# Create the drum notes
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (61, 2.625),
    (62, 3.0), (63, 3.375), (60, 3.75), (61, 4.125),
    (62, 4.5), (63, 4.875), (60, 5.25), (61, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (62, 2.0), (64, 2.0), (67, 2.0), (69, 2.0),
    # Bar 3: G7 (G, B, D, F)
    (71, 3.0), (73, 3.0), (76, 3.0), (78, 3.0),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 4.0), (63, 4.0), (67, 4.0), (69, 4.0)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    (62, 1.5), (64, 1.875), (67, 2.25), (69, 2.625),
    (62, 3.0), (64, 3.375), (67, 3.75), (69, 4.125),
    (62, 4.5), (64, 4.875), (67, 5.25), (69, 5.625)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=115, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
