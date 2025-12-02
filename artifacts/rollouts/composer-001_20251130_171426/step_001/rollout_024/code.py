
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
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.375), (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375), (38, 1.875, 0.375),
    # Hi-hat on every eighth
    (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (39, 1.5, 0.375), # Fm root
    (41, 1.875, 0.375), # b9
    (40, 2.25, 0.375), # 7
    (37, 2.625, 0.375), # b7
    (39, 3.0, 0.375), # Fm
    (41, 3.375, 0.375), # b9
    (40, 3.75, 0.375), # 7
    (37, 4.125, 0.375), # b7
    (39, 4.5, 0.375), # Fm
    (41, 4.875, 0.375), # b9
    (40, 5.25, 0.375), # 7
    (37, 5.625, 0.375), # b7
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 at beat 2
    (43, 2.25, 0.375), (41, 2.25, 0.375), (39, 2.25, 0.375), (37, 2.25, 0.375),
    # Bar 3: Fm7 at beat 2
    (43, 3.75, 0.375), (41, 3.75, 0.375), (39, 3.75, 0.375), (37, 3.75, 0.375),
    # Bar 4: Fm7 at beat 2
    (43, 5.25, 0.375), (41, 5.25, 0.375), (39, 5.25, 0.375), (37, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (36, 2.625, 0.375),
    (38, 1.875, 0.375), (38, 3.0, 0.375),
    (42, 1.5, 0.1875), (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875), (42, 2.8125, 0.1875),
    (42, 3.0, 0.1875),
    (36, 3.0, 0.375), (36, 4.125, 0.375),
    (38, 3.375, 0.375), (38, 4.5, 0.375),
    (42, 3.0, 0.1875), (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875), (42, 4.3125, 0.1875),
    (42, 4.5, 0.1875),
    (36, 4.5, 0.375), (36, 5.625, 0.375),
    (38, 4.875, 0.375), (38, 6.0, 0.375),
    (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875), (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F to Ab to Bb to F (hanging) — then repeat and resolve

sax_notes = [
    (43, 1.5, 0.375), # F
    (41, 1.875, 0.375), # Ab
    (40, 2.25, 0.375), # Bb
    (43, 2.625, 0.375), # F
    (43, 3.0, 0.375), # F
    (41, 3.375, 0.375), # Ab
    (40, 3.75, 0.375), # Bb
    (43, 4.125, 0.375), # F
    (43, 4.5, 0.375), # F
    (41, 4.875, 0.375), # Ab
    (40, 5.25, 0.375), # Bb
    (43, 5.625, 0.375) # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
