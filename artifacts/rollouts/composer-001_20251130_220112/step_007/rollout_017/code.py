
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G7
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.0, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)
    
    drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2, hihat5, hihat6, hihat7, hihat8])

# Sax (Dante): Motif with a question, a memory, a challenge
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
