
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches in Fm
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (53, 2.625),
    (55, 3.0), (53, 3.375), (51, 3.75), (53, 4.125),
    (53, 4.5), (51, 4.875), (50, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4 (in Fm)
piano_notes = [
    # Bar 2
    (60, 1.875), (64, 1.875), (62, 1.875), (66, 1.875), # F7
    # Bar 3
    (60, 3.375), (64, 3.375), (62, 3.375), (66, 3.375), # F7
    # Bar 4
    (60, 4.875), (64, 4.875), (62, 4.875), (66, 4.875)  # F7
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Drums: full bar with kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 1.875), (38, 2.25), (42, 2.25),
    (36, 2.625), (38, 2.875), (42, 2.875),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Sax line: one short motif, make it sing
sax_notes = [
    (60, 1.5), (62, 1.75), (60, 2.0), (62, 2.25),
    (60, 2.5), (62, 2.75), (60, 3.0), (62, 3.25),
    (60, 3.5), (62, 3.75), (60, 4.0), (62, 4.25),
    (60, 4.5), (62, 4.75), (60, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
