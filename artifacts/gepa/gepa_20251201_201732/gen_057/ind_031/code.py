
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)
instrument_sax = pretty_midi.Instrument(program=64)  # Tenor Sax
instrument_piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
instrument_bass = pretty_midi.Instrument(program=33)  # Double Bass
instrument_drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Time in seconds per bar
bar_length = 1.5
total_time = bar_length * 4

# -- Drums: Little Ray (Bar 1 only, set up with tension and space) --
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Dynamic contrast: soft on 1, explosive on 3, snare on 2 (loud), hihat soft

# Kick on 1 and 3 (beat 0 and 2)
kick_1 = pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)
instrument_drums.notes.extend([kick_1, kick_3])

# Snare on 2 and 4 (beat 1 and 3)
snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75)
snare_4 = pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5)
instrument_drums.notes.extend([snare_2, snare_4])

# Hi-hat on every eighth (soft, with some space)
hihat_1 = pretty_midi.Note(velocity=40, pitch=42, start=0.0, end=0.375)
hihat_2 = pretty_midi.Note(velocity=40, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=40, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=40, pitch=42, start=1.125, end=1.5)
instrument_drums.notes.extend([hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 2-4: Drums remain active, but more explosive and unpredictable
for bar in range(1, 4):
    start_time = bar * bar_length
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=np.random.randint(90, 110), pitch=36, start=start_time, end=start_time + 0.375)
    kick_3 = pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    instrument_drums.notes.extend([kick_1, kick_3])

    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=np.random.randint(85, 105), pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare_4 = pretty_midi.Note(velocity=np.random.randint(85, 105), pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    instrument_drums.notes.extend([snare_2, snare_4])

    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=np.random.randint(40, 60), pitch=42, 
                                 start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.375)
        instrument_drums.notes.append(hihat)

# -- Piano: Diane (Bars 2-4, open voicings, unresolved, emotional) --

# Bar 2: Dm7 (D F A C)
# Open voicing, D in root, A in 5th, C in 7th, F in 3rd
# Played on beat 2
chord_2 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75)
chord_2a = pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75)
chord_2b = pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75)
chord_2c = pretty_midi.Note(velocity=75, pitch=64, start=1.5, end=1.75)
instrument_piano.notes.extend([chord_2, chord_2a, chord_2b, chord_2c])

# Bar 3: G7sus4 (G C D F)
# Open voicing, G in root, C in 4th, D in 5th, F in 3rd
chord_3 = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25)
chord_3a = pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.25)
chord_3b = pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25)
chord_3c = pretty_midi.Note(velocity=75, pitch=74, start=3.0, end=3.25)
instrument_piano.notes.extend([chord_3, chord_3a, chord_3b, chord_3c])

# Bar 4: Cm7 (C Eb G Bb)
# Open voicing, C in root, G in 5th, Bb in 7th, Eb in 3rd
chord_4 = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75)
chord_4a = pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.75)
chord_4b = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75)
chord_4c = pretty_midi.Note(velocity=75, pitch=64, start=4.5, end=4.75)
instrument_piano.notes.extend([chord_4, chord_4a, chord_4b, chord_4c])

# -- Bass: Marcus (Bars 2-4, walking line, roots and fifths with chromatic approaches) --

# Bar 2: Dm7 — Root on 1, 5th on 2, chromatic down on 3, root on 4
bass_2 = pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.75)
bass_2a = pretty_midi.Note(velocity=65, pitch=67, start=1.875, end=2.125)
bass_2b = pretty_midi.Note(velocity=60, pitch=61, start=2.25, end=2.5)
bass_2c = pretty_midi.Note(velocity=65, pitch=62, start=2.625, end=2.875)
instrument_bass.notes.extend([bass_2, bass_2a, bass_2b, bass_2c])

# Bar 3: G7sus4 — Root on 1, 5th on 2, chromatic down on 3, root on 4
bass_3 = pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.25)
bass_3a = pretty_midi.Note(velocity=65, pitch=76, start=3.375, end=3.625)
bass_3b = pretty_midi.Note(velocity=60, pitch=70, start=3.75, end=4.0)
bass_3c = pretty_midi.Note(velocity=65, pitch=71, start=4.125, end=4.375)
instrument_bass.notes.extend([bass_3, bass_3a, bass_3b, bass_3c])

# Bar 4: Cm7 — Root on 1, 5th on 2, chromatic down on 3, root on 4
bass_4 = pretty_midi.Note(velocity=70, pitch=60, start=4.5, end=4.75)
bass_4a = pretty_midi.Note(velocity=65, pitch=67, start=4.875, end=5.125)
bass_4b = pretty_midi.Note(velocity=60, pitch=59, start=5.25, end=5.5)
bass_4c = pretty_midi.Note(velocity=65, pitch=60, start=5.625, end=5.875)
instrument_bass.notes.extend([bass_4, bass_4a, bass_4b, bass_4c])

# -- Sax: You (Bar 2-4, motif, haunting, with space) --

# Bar 2: Start the motif — a phrase that hangs
# D (62) on beat 1, F# (66) on beat 2, G (67) on beat 3, D (62) on beat 4, rest on beat 4
sax_2 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax_2a = pretty_midi.Note(velocity=95, pitch=66, start=1.875, end=2.25)
sax_2b = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625)
sax_2c = pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=3.0)
instrument_sax.notes.extend([sax_2, sax_2a, sax_2b, sax_2c])

# Bar 3: Rest, space, tension
# No notes — space is powerful

# Bar 4: Return with variation — a memory, a whisper
# D (62) on beat 1, F# (66) on beat 2, G (67) on beat 3, D# (64) on beat 4
sax_4 = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875)
sax_4a = pretty_midi.Note(velocity=85, pitch=66, start=4.875, end=5.25)
sax_4b = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625)
sax_4c = pretty_midi.Note(velocity=75, pitch=64, start=5.625, end=6.0)
instrument_sax.notes.extend([sax_4, sax_4a, sax_4b, sax_4c])

# Add all instruments to the MIDI
pm.instruments.append(instrument_sax)
pm.instruments.append(instrument_piano)
pm.instruments.append(instrument_bass)
pm.instruments.append(instrument_drums)

# Save MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
