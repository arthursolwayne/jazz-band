
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (37, 1.5), (38, 1.875), (39, 2.25), (40, 2.625),  # F7 chord
    (41, 3.0), (42, 3.375), (43, 3.75), (44, 4.125),  # B7 chord
    (45, 4.5), (46, 4.875), (47, 5.25), (48, 5.625)   # E7 chord
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (59, 2.25), (61, 2.25), (64, 2.25), (62, 2.25),  # F7 (F, A, C, Bb)
    # Bar 3: B7 on beat 2
    (71, 3.75), (73, 3.75), (76, 3.75), (74, 3.75),  # B7 (B, D#, F#, A)
    # Bar 4: E7 on beat 2
    (64, 5.25), (66, 5.25), (69, 5.25), (67, 5.25)   # E7 (E, G#, B, D)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F -> G -> A -> F (motif), then pause, then repeat with a twist
sax_notes = [
    (59, 1.5), (60, 1.875), (61, 2.25), (59, 2.625),  # Motif
    (59, 3.0), (60, 3.375), (61, 3.75), (62, 4.125),  # Motif with twist
    (61, 4.5), (60, 4.875), (59, 5.25), (57, 5.625)   # Resolution
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
