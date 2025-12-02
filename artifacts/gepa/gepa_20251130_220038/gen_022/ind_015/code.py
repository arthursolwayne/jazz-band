
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm (F, Gb, Ab, Bb, B, C, Db, Eb)
# Chromatic approach to each chord, never same note twice
bass_notes = [
    (65, 1.5, 0.375), (64, 1.875, 0.375), (62, 2.25, 0.375), (60, 2.625, 0.375),
    (61, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375), (58, 4.125, 0.375),
    (59, 4.5, 0.375), (60, 4.875, 0.375), (62, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, comp in Fm
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (53, 2.25, 0.1875), (50, 2.25, 0.1875), (57, 2.25, 0.1875), (55, 2.25, 0.1875),
    (53, 2.625, 0.1875), (50, 2.625, 0.1875), (57, 2.625, 0.1875), (55, 2.625, 0.1875),
    
    # Bar 3: Bb7 on 2 and 4
    (58, 3.75, 0.1875), (55, 3.75, 0.1875), (60, 3.75, 0.1875), (58, 3.75, 0.1875),
    (58, 4.125, 0.1875), (55, 4.125, 0.1875), (60, 4.125, 0.1875), (58, 4.125, 0.1875),
    
    # Bar 4: Eb7 on 2 and 4
    (51, 5.25, 0.1875), (48, 5.25, 0.1875), (53, 5.25, 0.1875), (51, 5.25, 0.1875),
    (51, 5.625, 0.1875), (48, 5.625, 0.1875), (53, 5.625, 0.1875), (51, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (Bars 2-4)
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    snare_start = start + 0.375
    hihat_start = start
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    hihat_notes = [pretty_midi.Note(velocity=110, pitch=42, start=hihat_start + i * 0.1875, end=hihat_start + i * 0.1875 + 0.1875) for i in range(8)]
    drums.notes.append(kick_note)
    drums.notes.append(snare_note)
    drums.notes.extend(hihat_notes)

# Dante: Your moment — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (62), Bb (60), F (65) — but start it, leave it hanging, come back and finish it
sax_notes = [
    (65, 1.5, 0.375), (62, 1.875, 0.375), (60, 2.25, 0.375),
    (65, 4.5, 0.375), (62, 4.875, 0.375), (60, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
