
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),
    (62, 3.0), (63, 3.375), (60, 3.75), (62, 4.125),
    (62, 4.5), (63, 4.875), (60, 5.25), (62, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F# on beat 2, A on beat 4)
    (62, 2.25), (67, 2.25),
    (62, 3.0), (67, 3.0),
    # Bar 3: Gm7 (Bb on beat 2, D on beat 4)
    (60, 3.75), (65, 3.75),
    (60, 4.5), (65, 4.5),
    # Bar 4: Cm7 (Eb on beat 2, G on beat 4)
    (64, 5.25), (69, 5.25),
    (64, 6.0), (69, 6.0)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Melody - one short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    # Bar 2: Start with D (62) on beat 1, then F (65) on beat 2
    (62, 1.5), (65, 1.875),
    # Bar 3: A (67) on beat 1, rest on beat 2
    (67, 3.0), (67, 3.375),
    # Bar 4: C (64) on beat 1, D (62) on beat 3, F (65) on beat 4
    (64, 4.5), (62, 4.875), (65, 5.625)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
midi.dump()
