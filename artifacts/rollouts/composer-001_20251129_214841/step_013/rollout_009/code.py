
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.375),
    (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375),
    (38, 2.25, 0.375),
    # Hihat on every eighth
    (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875),
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time signature: 4/4, 120 BPM = 0.5s per beat

# Bass line: Marcus (walking line, chromatic approaches, no repeated notes)
bass_notes = [
    # Bar 2: C -> D -> Eb -> F
    (48, 1.5, 0.5),
    (50, 2.0, 0.5),
    (49, 2.5, 0.5),
    (52, 3.0, 0.5),
    # Bar 3: G -> Ab -> A -> Bb
    (55, 3.5, 0.5),
    (56, 4.0, 0.5),
    (57, 4.5, 0.5),
    (58, 5.0, 0.5),
    # Bar 4: C -> D -> Eb -> F (resolve)
    (48, 5.5, 0.5),
    (50, 6.0, 0.5),
    (49, 6.5, 0.5),
    (52, 7.0, 0.5),
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: C7 on beat 2
    (60, 2.0, 0.5),
    (64, 2.0, 0.5),
    (67, 2.0, 0.5),
    (69, 2.0, 0.5),
    # Bar 3: F7 on beat 2
    (65, 4.0, 0.5),
    (69, 4.0, 0.5),
    (71, 4.0, 0.5),
    (72, 4.0, 0.5),
    # Bar 4: C7 on beat 2
    (60, 6.0, 0.5),
    (64, 6.0, 0.5),
    (67, 6.0, 0.5),
    (69, 6.0, 0.5),
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: Dante (one short motif, make it sing)
# C (60) -> Eb (62) -> D (62) -> Bb (67) -> C (60) -> D (62) -> Eb (64)
# Start at bar 2, beat 1
sax_notes = [
    (60, 1.5, 0.375),
    (62, 1.875, 0.375),
    (62, 2.25, 0.375),
    (67, 2.625, 0.375),
    (60, 2.625, 0.375),
    (62, 2.75, 0.375),
    (64, 2.875, 0.375),
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums continue for bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    kick_start = 1.5 + (bar - 1) * 1.5
    kick_start_1 = kick_start
    kick_start_3 = kick_start + 1.125
    dr = pretty_midi.Note(velocity=100, pitch=36, start=kick_start_1, end=kick_start_1 + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=36, start=kick_start_3, end=kick_start_3 + 0.375)
    drums.notes.append(dr)

# Snare on 2 and 4
for bar in [2, 3, 4]:
    snare_start = 1.5 + (bar - 1) * 1.5
    snare_start_2 = snare_start + 0.75
    snare_start_4 = snare_start + 2.25
    dr = pretty_midi.Note(velocity=100, pitch=38, start=snare_start_2, end=snare_start_2 + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=38, start=snare_start_4, end=snare_start_4 + 0.375)
    drums.notes.append(dr)

# Hihat on every eighth
for bar in [2, 3, 4]:
    start = 1.5 + (bar - 1) * 1.5
    for i in range(8):
        time = start + i * 0.1875
        dr = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1875)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
