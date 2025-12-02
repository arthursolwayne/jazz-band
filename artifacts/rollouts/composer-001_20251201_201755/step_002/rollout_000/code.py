
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (36, 1.125, 0.375),
    (38, 1.5, 0.375), (42, 1.5, 0.1875),
]

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), # F
    (40, 1.875, 0.375), # Ab
    (38, 2.25, 0.375), # F
    (41, 2.625, 0.375), # Bb
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 0.375), (55, 1.5, 0.375), (57, 1.5, 0.375), (60, 1.5, 0.375),
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax: Motif - Start with a short phrase, leave it hanging
sax_notes = [
    (62, 1.5, 0.375), # G
    (60, 1.875, 0.375), # F
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (42, 3.0, 0.375), # D
    (40, 3.375, 0.375), # Ab
    (42, 3.75, 0.375), # D
    (43, 4.125, 0.375), # Eb
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (58, 3.0, 0.375), (62, 3.0, 0.375), (53, 3.0, 0.375), (55, 3.0, 0.375),
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax: Motif continuation
sax_notes = [
    (62, 3.0, 0.375), # G
    (60, 3.375, 0.375), # F
    (58, 3.75, 0.375), # Eb
    (60, 4.125, 0.375), # F
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (38, 4.5, 0.375), # F
    (40, 4.875, 0.375), # Ab
    (38, 5.25, 0.375), # F
    (41, 5.625, 0.375), # Bb
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 4.5, 0.375), (55, 4.5, 0.375), (57, 4.5, 0.375), (60, 4.5, 0.375),
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax: Motif completion
sax_notes = [
    (62, 4.5, 0.375), # G
    (60, 4.875, 0.375), # F
    (58, 5.25, 0.375), # Eb
    (60, 5.625, 0.375), # F
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (36, 2.625, 0.375),
    (38, 3.0, 0.375), (42, 3.0, 0.1875),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (36, 4.125, 0.375),
    (38, 4.5, 0.375), (42, 4.5, 0.1875),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (36, 5.625, 0.375),
    (38, 6.0, 0.375), (42, 6.0, 0.1875),
]

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
