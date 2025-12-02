
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full band enters
# Sax: Motif - Fm7 -> Ab7 -> Bb7 -> Cm7 (F, Ab, Bb, C)
# Start with F, then leave it hanging on Ab

sax_notes = [
    (84, 1.5),   # F
    (87, 1.875), # Ab
    (88, 2.25),  # Bb
    (87, 2.625), # Ab (rest on 3rd beat)
    (88, 3.0),   # Bb (bring it back in)
    (84, 3.375), # F
    (87, 3.75),  # Ab
    (88, 4.125), # Bb
    (87, 4.5),   # Ab (rest on 3rd beat)
    (88, 4.875), # Bb (bring it back in)
    (84, 5.25),  # F
    (87, 5.625), # Ab
    (88, 6.0)    # Bb (resolve on 4th beat)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (64, 1.5),   # F
    (65, 1.875), # Gb
    (65, 2.25),  # Gb
    (64, 2.625), # F
    (64, 3.0),   # F
    (65, 3.375), # Gb
    (65, 3.75),  # Gb
    (64, 4.125), # F
    (64, 4.5),   # F
    (65, 4.875), # Gb
    (65, 5.25),  # Gb
    (64, 5.625), # F
    (64, 6.0)    # F
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db)
    (84, 1.875), (87, 1.875), (88, 1.875), (85, 1.875),
    # Bar 3: Ab7 (Ab, C, Db, F)
    (87, 2.625), (90, 2.625), (85, 2.625), (84, 2.625),
    # Bar 4: Bb7 (Bb, D, Eb, F)
    (88, 3.75), (92, 3.75), (93, 3.75), (84, 3.75),
    # Bar 4: Cm7 (C, Eb, F, Ab)
    (92, 4.5), (93, 4.5), (84, 4.5), (87, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
