
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3 (0.0s, 1.125s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.25),
    # Snare on 2 and 4 (0.375s, 1.5s)
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # F (1.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),
    # Bb (1.75s)
    pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=2.0),
    # D (2.0s)
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.25),
    # F (2.25s)
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5),
    # F# (chromatic approach to G) (2.5s)
    pretty_midi.Note(velocity=80, pitch=54, start=2.5, end=2.75),
    # G (2.75s)
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on last
piano_notes = [
    # Bar 2 - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    # Bar 3 - Bbmaj7 (Bb, D, F, A)
    pretty_midi.Note(velocity=80, pitch=58, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),
    # Bar 4 - D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=59, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),
    # Resolve on last bar
    pretty_midi.Note(velocity=85, pitch=53, start=2.75, end=3.0),
    pretty_midi.Note(velocity=85, pitch=65, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: F (start 1.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.625),
    # Bar 3: Bb (start 2.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),
    # Bar 4: D (start 2.5s)
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.625),
    # Bar 4: F (start 2.875s)
    pretty_midi.Note(velocity=100, pitch=66, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes_bar3 = [
    # Kick on 1 and 3 (3.0s, 4.125s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.25),
    # Snare on 2 and 4 (3.375s, 4.5s)
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes_bar3)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes_bar4 = [
    # F (4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),
    # Bb (4.75s)
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),
    # D (5.0s)
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),
    # F (5.25s)
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),
    # F# (chromatic approach to G) (5.5s)
    pretty_midi.Note(velocity=80, pitch=54, start=5.5, end=5.75),
    # G (5.75s)
    pretty_midi.Note(velocity=90, pitch=55, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes_bar4)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes_bar4 = [
    # Resolve on Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    # Keep chord for full bar
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    # Keep chord for full bar
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    # Keep chord for full bar
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),
    # Keep chord for full bar
    pretty_midi.Note(velocity=80, pitch=53, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=55, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),
    # Keep chord for full bar
    pretty_midi.Note(velocity=80, pitch=53, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=55, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes_bar4)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes_bar4 = [
    # Kick on 1 and 3 (4.5s, 5.625s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.75),
    # Snare on 2 and 4 (4.875s, 6.0s)
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes_bar4)

# Bar 4: Sax (4.5 - 6.0s)
sax_notes_bar4 = [
    # Bar 4: F (start 4.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.625),
    # Bar 4: Bb (start 4.875s)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),
    # Bar 4: D (start 5.25s)
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.375),
    # Bar 4: F (start 5.625s)
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.75),
    # Bar 4: Bb (start 5.875s)
    pretty_midi.Note(velocity=100, pitch=71, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
