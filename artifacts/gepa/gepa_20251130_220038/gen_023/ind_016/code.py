
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
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (64, 1.5), (65, 1.875), (63, 2.25), (61, 2.625),
    (62, 3.0), (64, 3.375), (65, 3.75), (63, 4.125),
    (61, 4.5), (62, 4.875), (64, 5.25), (65, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    (53, 1.875), (50, 1.875), (57, 1.875), (55, 1.875),
    # Bar 3: Bb7
    (62, 3.375), (59, 3.375), (64, 3.375), (62, 3.375),
    # Bar 4: Eb7
    (60, 4.875), (57, 4.875), (62, 4.875), (60, 4.875)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C (1.5s) then rest, then F, Ab, Bb, C (4.5s)
sax_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (59, 2.625),
    (53, 4.5), (55, 4.875), (57, 5.25), (59, 5.625)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drum fill in bar 4
drum_notes = [
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
