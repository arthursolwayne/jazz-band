
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
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
# Bar 2: D2, G2, D2, F#2 (chromatic approach to G2)
# Bar 3: D2, A2, G2, A2
# Bar 4: D2, C#2 (chromatic approach to D2), D2, F#2
bar2_start = 1.5
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=41, start=bar2_start + 1.125, end=bar2_start + 1.5),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=45, start=bar2_start + 1.875, end=bar2_start + 2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=45, start=bar2_start + 2.625, end=bar2_start + 3.0),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=40, start=bar2_start + 3.375, end=bar2_start + 3.75),
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=80, pitch=41, start=bar2_start + 4.125, end=bar2_start + 4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
# Bar 3: Gm7 (G Bb D F)
# Bar 4: Cm7 (C Eb G Bb)
bar2_start = 1.5
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start, end=bar2_start + 0.375),
    # Bar 3: Gm7
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=74, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=76, start=bar2_start + 1.5, end=bar2_start + 1.875),
    # Bar 4: Cm7
    pretty_midi.Note(velocity=80, pitch=60, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=63, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start + 3.0, end=bar2_start + 3.375),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: continue the pattern
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5
for bar_start in [bar2_start, bar3_start, bar4_start]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    for note in drum_notes:
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: D4, F4, Bb4, D4 (Dm scale, but with a twist)
# Play first note (D4), leave it hanging, then come back and finish it
sax_notes = [
    # First note: D4 (start at 1.5s, end at 2.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    # Rest of melody: F4, Bb4, D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
