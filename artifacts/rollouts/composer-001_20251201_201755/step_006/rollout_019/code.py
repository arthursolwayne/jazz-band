
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
drum_note_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_note_kick, drum_note_snare, drum_note_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Dm7 (D F A C)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G Bb D F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # F5
]
# Bar 4: A7 (A C# E G)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # C#5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # G5
]
# Resolve on the last bar to Dm7
piano_notes_bar4_resolve = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4 + piano_notes_bar4_resolve)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
sax_notes = [
    # Bar 2: Start motif (D4, F4, A4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.9375),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.1875),  # A4
    # Bar 3: Leave it hanging (nothing)
    # Bar 4: Return and finish motif (C5, D5)
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.6875),  # C5
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.9375),  # D5
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25)
    hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)
    hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
