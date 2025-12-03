
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0), # G2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125), # E2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # D2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0), # G2
]
bass.notes.extend(bass_notes)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0), # C5
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5), # F5
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0), # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0), # Bb4
    # Bar 5: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5), # C5
    # Bar 6: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0), # F5
    # Bar 7: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.5), # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.5), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5), # Bb4
    # Bar 8: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0), # C5
    # Bar 9: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.5), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.5), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.5), # F5
    # Bar 10: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0), # C4
    pretty_midi.Note(velocity=100, pitch=63, start=5.5, end=6.0), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=6.0), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=6.0), # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif start
    pretty_midi.Note(velocity=110, pitch=68, start=1.5, end=1.75), # E4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0), # D4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.25), # E4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5), # D4
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=2.75, end=3.0), # E4
    # Bar 5: Repeat motif
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25), # E4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5), # D4
    # Bar 6: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75), # E4
    # Bar 7: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0), # D4
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=4.25, end=4.5), # E4
    # Bar 8: Repeat motif
    pretty_midi.Note(velocity=110, pitch=68, start=4.5, end=4.75), # E4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0), # D4
    # Bar 9: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.25), # E4
    # Bar 10: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5), # D4
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=5.75, end=6.0), # E4
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
