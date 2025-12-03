
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Bar 2: F (chromatic approach to G)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    # Bar 2: G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # Bar 3: C (root of Dm7)
    pretty_midi.Note(velocity=90, pitch=40, start=2.5, end=2.875),
    # Bar 3: E (chromatic approach to F)
    pretty_midi.Note(velocity=90, pitch=43, start=2.875, end=3.125),
    # Bar 3: F2 (fifth of C)
    pretty_midi.Note(velocity=90, pitch=41, start=3.125, end=3.5),
    # Bar 4: Bb (chromatic approach to B)
    pretty_midi.Note(velocity=90, pitch=37, start=3.5, end=3.875),
    # Bar 4: B (fifth of F)
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.25),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=4.25, end=4.625),
    # Bar 4: F (chromatic approach to G)
    pretty_midi.Note(velocity=90, pitch=41, start=4.625, end=4.875),
    # Bar 4: G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C) - open voicing
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C5
]
# Bar 3: Gm7 (G, Bb, D, F) - open voicing
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875), # G4
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.875), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.875), # F5
]
# Bar 4: Cm7 (C, Eb, G, Bb) - open voicing
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.875), # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.875), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875), # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.875), # Bb4
]
piano_notes = piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Bar 2
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*0.375 + 0.75, end=1.5 + i*0.375 + 0.75 + 0.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.1875)
    drums.notes.extend([kick, snare, hihat])
# Bar 3
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=2.5 + i*0.375, end=2.5 + i*0.375 + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=2.5 + i*0.375 + 0.75, end=2.5 + i*0.375 + 0.75 + 0.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=2.5 + i*0.375, end=2.5 + i*0.375 + 0.1875)
    drums.notes.extend([kick, snare, hihat])
# Bar 4
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=3.5 + i*0.375, end=3.5 + i*0.375 + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=3.5 + i*0.375 + 0.75, end=3.5 + i*0.375 + 0.75 + 0.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=3.5 + i*0.375, end=3.5 + i*0.375 + 0.1875)
    drums.notes.extend([kick, snare, hihat])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Eb, F, G (1.5 - 2.0s), then G, A, Bb, C (3.5 - 4.0s)
# Bar 2
sax_notes_bar2 = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=110, pitch=63, start=1.75, end=2.0), # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5), # G4
]
# Bar 4
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0), # A4
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25), # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5), # C4
]
sax_notes = sax_notes_bar2 + sax_notes_bar4
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
