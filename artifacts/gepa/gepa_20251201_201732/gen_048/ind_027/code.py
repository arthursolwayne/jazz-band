
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
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Roots and fifths with chromatic approaches
# Fm: F, C, Ab, D, Bb, E, Db, G
# Bar 2: F, Ab, F, G
bass_notes = [
    (48, 1.5), (53, 1.5), (48, 1.875), (50, 1.875),
    # Bar 3: C, Bb, C, D
    (55, 3.0), (50, 3.0), (55, 3.375), (57, 3.375),
    # Bar 4: Ab, G, Ab, Bb
    (53, 4.5), (50, 4.5), (53, 4.875), (48, 4.875)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano (Diane): Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb) => F, Ab, C, Eb
# Bar 3: Bb7 (Bb, D, F, Ab) => Bb, D, F, Ab
# Bar 4: Gm7 (G, Bb, D, F) => G, Bb, D, F
piano_notes = [
    # Bar 2
    (48, 1.5), (53, 1.5), (55, 1.5), (50, 1.5),
    # Bar 3
    (50, 3.0), (55, 3.0), (57, 3.0), (53, 3.0),
    # Bar 4
    (50, 4.5), (53, 4.5), (57, 4.5), (55, 4.5)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note_obj)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (42, 2.75), (42, 2.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    (42, 4.25), (42, 4.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625),
    (42, 5.75), (42, 5.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm: F, Ab, Eb, C (Fm7)
# Motif: F (1.5), Ab (1.625), Eb (1.75), rest (1.875)
# Then repeat: F (3.0), Ab (3.125), rest (3.25), Eb (3.375)
# Then: C (4.5), rest (4.625), F (4.75), rest (4.875)

sax_notes = [
    (48, 1.5, 0.125), (53, 1.625, 0.125), (50, 1.75, 0.125),
    (48, 3.0, 0.125), (53, 3.125, 0.125), (50, 3.375, 0.125),
    (55, 4.5, 0.125), (55, 4.75, 0.125)
]
for note, time, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
