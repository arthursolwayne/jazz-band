
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (MIDI 65)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    # Chromatic approach to Bb (MIDI 62)
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.5),
    # Bar 3: Bb (MIDI 62)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.875),
    # Chromatic approach to Eb (MIDI 59)
    pretty_midi.Note(velocity=80, pitch=58, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=59, start=3.125, end=3.5),
    # Bar 4: Eb (MIDI 59)
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=3.875),
    # Chromatic approach to Ab (MIDI 56)
    pretty_midi.Note(velocity=80, pitch=55, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=56, start=4.125, end=4.5),
    # Bar 5: Ab (MIDI 56)
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),
    # Chromatic approach to D (MIDI 53)
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=53, start=5.125, end=5.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.5),
    # Bar 4: Ebmaj7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),
    # Bar 5: Abmaj7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: D (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Bar 2: F (MIDI 65) on beat 2
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),
    # Bar 2: G (MIDI 67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),
    # Bar 2: D (MIDI 62) on beat 4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    # Bar 3: F (MIDI 65) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.875),
    # Bar 3: G (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),
    # Bar 3: A (MIDI 69) on beat 3
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),
    # Bar 3: D (MIDI 62) on beat 4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
    # Bar 4: F (MIDI 65) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.875),
    # Bar 4: G (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=6.0, end=6.25),
    # Bar 4: D (MIDI 62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=6.5, end=6.75),
    # Bar 4: F (MIDI 65) on beat 4
    pretty_midi.Note(velocity=110, pitch=65, start=7.0, end=7.25),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
