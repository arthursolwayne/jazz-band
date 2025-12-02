
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Hihat on every eighth
for i in range(0, 6):
    pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=(i + 1) * 0.375).append_to_instrument(drums)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Diane on piano, 7th chords, comp on 2 and 4
# F7 on beat 1, A7 on beat 3
piano_notes = [
    # F7: F, A, C, E
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # E
    # A7: A, C#, E, G#
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875), # A
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=2.875), # C#
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=2.875), # E
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=2.875), # G#
]
for note in piano_notes:
    piano.notes.append(note)

# Marcus on bass: Walking line in F, chromatic approach
# F - Gb - G - A - Bb - B - C - Db - D - Eb - E - F#
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=80, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=81, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=82, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Dante on sax: Motif in F, short and singable
# F - G - Bb - C - F (call and response)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375).append_to_instrument(drums)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125).append_to_instrument(drums)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5).append_to_instrument(drums)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875).append_to_instrument(drums)
    # Hihat on every eighth
    for i in range(0, 6):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + (i + 1) * 0.375).append_to_instrument(drums)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
