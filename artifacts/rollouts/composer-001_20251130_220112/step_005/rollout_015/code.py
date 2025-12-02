
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
    (36, 0.0), (38, 0.375), (42, 0.375), (42, 0.75),
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (55, 2.625),
    (53, 3.0), (51, 3.375), (50, 3.75), (55, 4.125),
    (53, 4.5), (51, 4.875), (50, 5.25), (55, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Fm7
    (53, 2.0), (49, 2.0), (51, 2.0), (57, 2.0),
    # Bar 2, beat 4: Bb7
    (58, 2.5), (54, 2.5), (56, 2.5), (62, 2.5),
    # Bar 3, beat 2: Fm7
    (53, 3.5), (49, 3.5), (51, 3.5), (57, 3.5),
    # Bar 3, beat 4: Bb7
    (58, 4.0), (54, 4.0), (56, 4.0), (62, 4.0),
    # Bar 4, beat 2: Fm7
    (53, 5.0), (49, 5.0), (51, 5.0), (57, 5.0),
    # Bar 4, beat 4: Bb7
    (58, 5.5), (54, 5.5), (56, 5.5), (62, 5.5)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (42, 2.25),
    (36, 2.625), (38, 3.0), (42, 3.0), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125), (42, 4.5),
    (36, 4.875), (38, 5.25), (42, 5.25), (42, 5.625)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Dante: Short motif starting at bar 2, beat 1
# 53 (F), 51 (Eb), 50 (D), 53 (F) - 4 notes, 0.375s each
sax_notes = [
    (53, 2.0), (51, 2.375), (50, 2.75), (53, 3.125)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_shorter_intro.mid')
