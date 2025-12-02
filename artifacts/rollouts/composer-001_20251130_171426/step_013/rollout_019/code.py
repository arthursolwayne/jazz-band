
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
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (39, 1.5), (40, 1.875), (39, 2.25), (38, 2.625),
    # Bar 3
    (37, 3.0), (38, 3.375), (37, 3.75), (36, 4.125),
    # Bar 4
    (35, 4.5), (36, 4.875), (35, 5.25), (34, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (42, 1.875), (46, 1.875), (47, 1.875), (50, 1.875),
    (42, 2.625), (46, 2.625), (47, 2.625), (50, 2.625),
    # Bar 3
    (42, 3.375), (46, 3.375), (47, 3.375), (50, 3.375),
    (42, 4.125), (46, 4.125), (47, 4.125), (50, 4.125),
    # Bar 4
    (42, 4.875), (46, 4.875), (47, 4.875), (50, 4.875),
    (42, 5.625), (46, 5.625), (47, 5.625), (50, 5.625)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C (from 1.5s)
# Repeat: F, Ab, Bb, C (from 3.75s)
# End: F, Ab, Bb, C (from 5.25s)

sax_notes = [
    # First motif
    (53, 1.5), (55, 1.875), (57, 2.25), (59, 2.625),
    # Repeat
    (53, 3.75), (55, 4.125), (57, 4.5), (59, 4.875),
    # End
    (53, 5.25), (55, 5.625), (57, 6.0), (59, 6.375)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
