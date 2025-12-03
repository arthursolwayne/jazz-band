
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everybody in. Sax melody
# Dm7 -> Gm7 -> Cm7 -> F7
# Sax motif: D - F - G - Bb (Dm7 arpeggio with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),  # A2 (fifth of Dm)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Full band
# Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.625 + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.0 + 0.375),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625 + 0.75, end=2.625 + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + 0.75, end=3.0 + 1.125),
    
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.625 + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625 + 0.375, end=2.625 + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625 + 0.75, end=2.625 + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625 + 1.125, end=2.625 + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0 + 0.375, end=3.0 + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0 + 0.75, end=3.0 + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0 + 1.125, end=3.0 + 1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Sax repeats the motif with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.625 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625 + 0.375, end=2.625 + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625 + 0.75, end=2.625 + 1.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625 + 1.125, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bass repeats walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.625 + 0.375),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625 + 0.375, end=2.625 + 0.75),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625 + 0.75, end=2.625 + 1.125),  # F#2
    pretty_midi.Note(velocity=100, pitch=44, start=2.625 + 1.125, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano resolves on F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
