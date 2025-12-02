
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0,螃蟹=120)]

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
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Start of motif
sax_note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0)
sax_note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3])

# BASS: Walking line
bass_note1 = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75)
bass_note2 = pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0)
bass_note3 = pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25)
bass_note4 = pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# PIANO: 7th chords, comp on 2 and 4
piano_note1 = pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0)
piano_note2 = pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0)
piano_note3 = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0)
piano_note4 = pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# DRUMS: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick1 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drum_snare1 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drum_hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)
drum_hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
drum_hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625)
drum_hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
drums.notes.extend([drum_kick1, drum_kick2, drum_snare1, drum_snare2,
                    drum_hihat1, drum_hihat2, drum_hihat3, drum_hihat4])

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Continue motif
sax_note4 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25)
sax_note5 = pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5)
sax_note6 = pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0)
sax.notes.extend([sax_note4, sax_note5, sax_note6])

# BASS: Walking line
bass_note5 = pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25)
bass_note6 = pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.5)
bass_note7 = pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75)
bass_note8 = pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# PIANO: 7th chords, comp on 2 and 4
piano_note5 = pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5)
piano_note6 = pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5)
piano_note7 = pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5)
piano_note8 = pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# DRUMS: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
drum_hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
drum_hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
drum_hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
drums.notes.extend([drum_kick3, drum_kick4, drum_snare3, drum_snare4,
                    drum_hihat5, drum_hihat6, drum_hihat7, drum_hihat8])

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Finish motif
sax_note7 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75)
sax_note8 = pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0)
sax_note9 = pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5)
sax_note10 = pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=6.0)
sax.notes.extend([sax_note7, sax_note8, sax_note9, sax_note10])

# BASS: Walking line
bass_note9 = pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75)
bass_note10 = pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0)
bass_note11 = pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25)
bass_note12 = pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5)
bass_note13 = pretty_midi.Note(velocity=80, pitch=71, start=5.5, end=6.0)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12, bass_note13])

# PIANO: 7th chords, comp on 2 and 4
piano_note9 = pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0)
piano_note10 = pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0)
piano_note11 = pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0)
piano_note12 = pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# DRUMS: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick5 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick6 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drum_snare5 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_snare6 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drum_hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
drum_hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
drum_hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
drum_hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
drums.notes.extend([drum_kick5, drum_kick6, drum_snare5, drum_snare6,
                    drum_hihat9, drum_hihat10, drum_hihat11, drum_hihat12])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
